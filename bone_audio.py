"""bone_audio.py"""

import os
import re
import logging
import warnings
import sys
import contextlib
from typing import Dict, List
from bone_types import Prisma

# --- SILENCE THE LIBRARIES ---
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TQDM_DISABLE"] = "True"
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

class TheVocalCords:
    """
    The Direct-Inference Audio Engine.
    Parses multi-agent scripts and runs them through the local Kokoro neural network.
    Stitches all dialogue segments into a single master podcast file.
    """
    def __init__(self, events_ref=None):
        self.events = events_ref
        self.voice_map = {
            "BENEDICT": "am_adam",
            "JESTER": "am_puck",
            "STAGE MANAGER": "af_sky",
            "GORDON": "am_michael",
            "DEFAULT": "af_bella"
        }
        self.pipeline = None
        self.sf = None

    @staticmethod
    def strip_ansi(text: str) -> str:
        """Strips terminal color codes from the script."""
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def parse_script(self, script_text: str) -> List[Dict[str, str]]:
        """Extracts the speaker tags and their corresponding dialogue blocks."""
        clean_text = self.strip_ansi(script_text)
        pattern = re.compile(r'^\[(.*?)]\s*\n(.*?)(?=\n\[|\Z)', re.MULTILINE | re.DOTALL)
        segments = []
        for match in pattern.finditer(clean_text):
            speaker = match.group(1).split(" (")[0].strip().upper()
            dialogue = match.group(2).strip()
            if dialogue:
                segments.append({"speaker": speaker, "text": dialogue})
        return segments

    def synthesize_podcast(self, file_path: str):
        """Generates a single combined audio file for the entire script."""
        if not os.path.exists(file_path):
            return

        with open(file_path, "r", encoding="utf-8") as f:
            script_text = f.read()

        segments = self.parse_script(script_text)
        if not segments:
            return

        output_dir = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        master_file = os.path.join(output_dir, f"{base_name}_MASTER.wav")

        combined_audio = []
        error_to_report = None

        # Redirection Context: We ONLY wrap the noisy library initialization and generation
        try:
            with open(os.devnull, 'w') as fnull:
                with contextlib.redirect_stdout(fnull), contextlib.redirect_stderr(fnull):
                    # 1. Initialize Pipeline (Lazy load)
                    if not self.pipeline:
                        from kokoro import KPipeline
                        import soundfile as sf
                        self.pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')
                        self.sf = sf

                    import numpy as np

                    # 2. Iterate through segments and accumulate audio buffers
                    for seg in segments:
                        speaker = seg["speaker"]
                        text = seg["text"]
                        voice = self.voice_map.get(speaker, self.voice_map["DEFAULT"])

                        generator = self.pipeline(text, voice=voice, speed=1.0)
                        for _, _, audio in generator:
                            combined_audio.append(audio)
                            # Add 0.3s of silence between speakers to let the debate breathe
                            combined_audio.append(np.zeros(int(24000 * 0.3)))

                    if combined_audio:
                        final_array = np.concatenate(combined_audio)
                        self.sf.write(master_file, final_array, 24000)

        except Exception as e:
            error_to_report = str(e)

        # 3. Reporting: This is OUTSIDE the redirect so Gordon can speak to you in the CLI
        if error_to_report:
            if self.events:
                self.events.log(f"{Prisma.RED}🎙️ AUDIO FAULT: {error_to_report}{Prisma.RST}", "SYS")
        elif combined_audio:
            if self.events:
                self.events.log(f"{Prisma.MAG}🎙️ MASTER PODCAST FORGED: {os.path.basename(master_file)}{Prisma.RST}", "SYS")