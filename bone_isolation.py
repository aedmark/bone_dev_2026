"""test_mode_isolation.py"""

import unittest
from bone_config import BonePresets
from bone_main import BoneAmanita
from bone_core import LoreManifest

class ModeIsolationTest(unittest.TestCase):
    def setUp(self):
        # Boot the system in a neutral state
        self.test_config = {
            "PROVIDER": "mock",
            "boot_mode": "CONVERSATION",
            "MAX_STAMINA": 100.0,
            "MAX_HEALTH": 100.0
        }
        self.engine = BoneAmanita(config=self.test_config)

    def tearDown(self):
        LoreManifest.get_instance().flush_cache()

    def generate_prompt_for_mode(self, mode_name: str) -> str:
        """Helper to hot-swap the mode and generate a raw system prompt."""
        # 1. Hot-swap the engine mode AND the cortex's internal state tracker
        self.engine.mode = mode_name
        self.engine.cortex.active_mode = mode_name # <-- THE CRITICAL FIX

        # 2. Gather the biological and physical state
        state = self.engine.cortex.gather_state({"physics": {"voltage": 50.0}})

        # 3. Compose the prompt
        return self.engine.cortex.composer.compose(
            state,
            "Testing mode isolation.",
            modifiers={"include_inventory": False}
        )

    def test_adventure_mode_isolation(self):
        prompt = self.generate_prompt_for_mode("ADVENTURE")

        self.assertIn("Object-Action Coupling", prompt, "Missing ADVENTURE core constraint.")
        self.assertIn("Exits:", prompt, "Missing ADVENTURE spatial formatting.")

        # Anti-bleed checks
        self.assertNotIn("Clinical, precise", prompt, "TECHNICAL formatting bled into ADVENTURE.")
        self.assertNotIn("Do not act like a Dungeon Master", prompt, "CONVERSATION constraint bled into ADVENTURE.")

    def test_conversation_mode_isolation(self):
        prompt = self.generate_prompt_for_mode("CONVERSATION")

        self.assertIn("Do not act like a Dungeon Master", prompt, "Missing CONVERSATION framing.")

        # Anti-bleed checks
        self.assertNotIn("Object-Action Coupling", prompt, "ADVENTURE mechanics bled into CONVERSATION.")
        self.assertNotIn("Exits:", prompt, "ADVENTURE spatial formatting bled into CONVERSATION.")
        self.assertNotIn("Clinical, precise", prompt, "TECHNICAL formatting bled into CONVERSATION.")

    def test_creative_mode_isolation(self):
        prompt = self.generate_prompt_for_mode("CREATIVE")

        # Assuming CREATIVE mode asks for prose or poetry based on system_prompts.json
        # Adjust these assertions to match your exact prompt library strings
        self.assertTrue(
            "prose" in prompt.lower() or "poetry" in prompt.lower() or "creative" in prompt.lower(),
            "Missing CREATIVE stylistic directives."
        )

        # Anti-bleed checks
        self.assertNotIn("Object-Action Coupling", prompt, "ADVENTURE mechanics bled into CREATIVE.")
        self.assertNotIn("Clinical, precise", prompt, "TECHNICAL formatting bled into CREATIVE.")

    def test_technical_mode_isolation(self):
        prompt = self.generate_prompt_for_mode("TECHNICAL")

        self.assertIn("Clinical, precise", prompt, "Missing TECHNICAL stylistic directives.")
        self.assertIn("Do not write prose", prompt, "Missing TECHNICAL anti-prose constraint.")

        # Anti-bleed checks
        self.assertNotIn("Object-Action Coupling", prompt, "ADVENTURE mechanics bled into TECHNICAL.")
        self.assertNotIn("Exits:", prompt, "ADVENTURE spatial formatting bled into TECHNICAL.")

if __name__ == "__main__":
    unittest.main()