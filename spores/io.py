"""spores/io.py

This module handles the physical storage and retrieval of "Spores" (session states).
If genetics.py handles the biological blueprint, this file handles the amber
that preserves the DNA. It ensures that memory states are safely written to
disk without risking data corruption during sudden system crashes or power loss.

Classes:
    - LocalFileSporeLoader: The primary interface for reading, writing, and pruning
      dormant memory states on the local file system.
"""

import json
import os
import tempfile
from typing import List, Tuple
from core import BoneJSONEncoder
from struts import ux_format
from constants import Prisma

class LocalFileSporeLoader:
    """
    Manages the Input/Output lifecycle of Spore files.
    Acts as the physical substrate layer, translating active memory graphs into
    dormant JSON structures and storing them safely on the disk.
    """
    def __init__(self, directory="memories"):
        # Establish the physical boundary for memory storage
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save_spore(self, filename, data):
        """
        Preserves the active memory state to disk using an atomic write pattern.

        [S]ynergetic Heuristic: We NEVER write directly over an existing memory file.
        If the process dies halfway through a direct write, the JSON is corrupted,
        and the spore is dead. Instead, we write to a temporary file, flush the buffer,
        and then execute an atomic OS-level replacement.
        """
        temp_path = filename

        # Ensure we are writing to the correct absolute or relative path
        if not os.path.isabs(filename) and not filename.startswith(
                os.path.join(self.directory, "")):
            final_path = os.path.join(self.directory, filename)
        else:
            final_path = filename

        # Ensure the sub-directories exist before we attempt to write
        os.makedirs(os.path.dirname(final_path), exist_ok=True)

        try:
            # 1. Create a secure temporary file in the same directory (prevents cross-device link errors)
            fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(final_path), text=True)

            with os.fdopen(fd, "w", encoding="utf-8") as f:
                # 2. Dump the data using our custom BoneJSONEncoder (handles sets, datetimes, etc.)
                json.dump(data, f, indent=2, cls=BoneJSONEncoder)

                # 3. Force the OS to flush internal buffers and write physically to the disk
                f.flush()
                os.fsync(f.fileno())

            # 4. Atomically replace the old file with the new complete file
            os.replace(temp_path, final_path)
            return final_path

        except (IOError, OSError, TypeError) as e:
            # If the write fails (disk full, permission error), catch it gracefully
            if msg := ux_format("spore_strings", "loader_save_err", e=e):
                print(f"{Prisma.RED}{msg}{Prisma.RST}")

            # Clean up the dangling temporary file so we don't leak storage
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return None

    @staticmethod
    def load_spore(filepath):
        """
        Thaws a dormant Spore file back into active memory dictionaries.
        Validates the file existence and structural integrity (valid JSON) before returning.
        """
        if not os.path.exists(filepath):
            if msg := ux_format("spore_strings", "loader_not_found", filepath=filepath):
                print(f"{Prisma.RED}{msg}{Prisma.RST}")
            return None

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            # Differentiate between a physical read error and biological corruption (bad JSON)
            err_type = "loader_corrupt" if isinstance(e, json.JSONDecodeError) else "loader_read_err"
            if msg := ux_format("spore_strings", err_type, filepath=filepath, e=e):
                print(f"{Prisma.RED}{msg}{Prisma.RST}")
            return None

    def list_spores(self) -> List[Tuple[str, float, str]]:
        """
        Surveys the memory directory and returns a chronologically sorted list
        of all valid session spores. Used for lineage tracking and cross-over selection.
        """
        if not os.path.exists(self.directory):
            return []

        try:
            files = []
            for filename in os.listdir(self.directory):
                # Filter for valid spore patterns to avoid parsing unrelated files
                if filename.endswith(".json") and filename.startswith("session_"):
                    full_path = os.path.join(self.directory, filename)
                    # Store as a tuple: (Absolute Path, Last Modified Timestamp, Raw Filename)
                    files.append((full_path, os.path.getmtime(full_path), filename))

            # Sort newest-first based on the timestamp
            return sorted(files, key=lambda x: x[1], reverse=True)

        except OSError:
            # Handle directory permission or disk read errors gracefully
            return []

    @staticmethod
    def delete_spore(filepath):
        """
        Prunes a specific spore from the disk permanently.
        """
        try:
            os.remove(filepath)
            return True
        except OSError:
            return False