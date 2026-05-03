"""tests/test_mechanics.py"""

from tests.base import BoneTestCase

class MechanicsTests(BoneTestCase):
    def test_session_guardian_crash_immersion(self):
        """
        THE SCHUR TEST: SessionGuardian must hide raw Python stack traces
        from the player during a fatal crash to preserve narrative immersion,
        unless specifically booted in TECHNICAL mode.
        """
        from mechanics.terminal import SessionGuardian
        from unittest.mock import MagicMock
        import sys
        import io

        mock_engine = MagicMock()
        mock_engine.boot_mode = "NARRATIVE"
        guardian = SessionGuardian(engine_ref=mock_engine)

        # Capture stdout to prevent the test suite from getting messy
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            # Simulate a fatal crash inside the context manager
            guardian.__exit__(ValueError, ValueError("A simulated fatal crash."), None)
        finally:
            sys.stdout = old_stdout

        output = captured_output.getvalue()

        # Assert that the raw traceback is hidden, but the graceful lattice message is shown
        self.assertNotIn("Traceback (most recent call last):", output,
                         "[FAIL] Raw stack trace leaked to the terminal in NARRATIVE mode!")
        self.assertIn("collapsed", output.lower(),
                      "[FAIL] SessionGuardian failed to print the graceful narrative crash message.")