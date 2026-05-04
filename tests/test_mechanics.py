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

    def test_protocol_gricean_membrane(self):
        """
        The Grice Test: Ensures The Pragmatist physically intercepts tropes,
        metabolic bloat, and linguistic hedging before the UI renders.
        """
        print("\n--- PROTOCOL 5: The Gricean Membrane ---")
        from mechanics.pragmatics import ThePragmatist

        pragmatist = ThePragmatist()

        # --- 1. Maxim of Quality (The Trope Breach) ---
        phys_state = {"narrative_drag": 0.0, "entropy": 0.0}
        bad_draft = "As an AI language model, I don't have feelings, but the sky is blue."
        mutated, needs_rewrite = pragmatist.enforce_maxims(bad_draft, "How are you?", phys_state, stamina=100.0)

        self.assertFalse(needs_rewrite,
                         "[FAIL] Quality breach should not trigger an LLM rewrite; it should mutate the text instantly.")
        self.assertIn("...", mutated,
                      "[FAIL] Pragmatist failed to execute the Trope Breach. Slop leaked through.")

        # --- 2. Maxim of Quantity (The Exhaustion Bloat) ---
        # Drag is high (10.0), which means the user is struggling. Max words allowed will be clamped to 20.
        phys_state = {"narrative_drag": 10.0, "entropy": 0.0}
        bloated_draft = "Word " * 50  # 50 words

        # Stamina is 20.0 (Exhausted). The LLM is trying to output 50 words.
        mutated, needs_rewrite = pragmatist.enforce_maxims(bloated_draft, "Tell me a story", phys_state, stamina=20.0)

        self.assertTrue(needs_rewrite,
                        "[FAIL] Pragmatist failed to trigger a rewrite on exhausted bloat. Cognitive overload imminent.")

        # --- 3. Maxim of Manner (The Hedging Stripper) ---
        # Chaos (entropy) is low (0.1). The system should speak with absolute structural certainty.
        phys_state = {"narrative_drag": 0.0, "entropy": 0.1}
        hedging_draft = "Perhaps it could be said that the sky is blue."
        mutated, needs_rewrite = pragmatist.enforce_maxims(hedging_draft, "What color is the sky?", phys_state,
                                                           stamina=100.0)

        self.assertNotIn("Perhaps", mutated, "[FAIL] Pragmatist failed to strip 'Perhaps'.")
        self.assertNotIn("it could be said that", mutated, "[FAIL] Pragmatist failed to strip 'it could be said that'.")
        self.assertIn("the sky is blue.", mutated,
                      "[FAIL] Pragmatist stripped too much and destroyed the bedrock logic.")

        print("  [SUCCESS] Gricean maxims successfully enforced.")