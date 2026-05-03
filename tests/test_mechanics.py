"""tests/test_mechanics.py"""

import unittest
from unittest.mock import patch, MagicMock
from tests.base import BoneTestCase

class MechanicsTests(BoneTestCase):
    @patch('mechanics.terminal.subprocess.run')
    def test_dignity_lock_destructive_intercept(self, mock_subprocess):
        """
        THE SCHUR TEST: Any attempt to execute highly destructive bash commands
        must trigger the Apoptotic Gate, blocking the subprocess entirely.
        """
        from mechanics.terminal import SessionGuardian as TerminalInterface

        terminal = TerminalInterface()

        lethal_commands = [
            "rm -rf /",
            "cat .env > public_leak.txt",
            "drop table users;"
        ]

        for cmd in lethal_commands:
            response = terminal.execute(cmd)

            # The subprocess must NEVER be called
            mock_subprocess.assert_not_called()

            # The system must return the specific Apoptotic friction response
            self.assertIn("APOPTOTIC_BLOCK", response, f"[FAIL] Terminal allowed destructive command: {cmd}")