"""
tests/test_chaos_engineering.py

The Structural Torture Suite.
These tests do not check for standard functionality. They inject terminal toxicity,
infinite loops, and catastrophic multi-threading failures to ensure the engine's
biological immune system (The Checkpoint Council, The Panic Room) successfully
prevents systemic death.
"""

import unittest
from unittest.mock import patch
from tests.base import BoneTestCase

class TestChaosEngineering(BoneTestCase):

    def test_vector_1_sycophancy_gravity_well(self):
        """
        THE JESTER'S TEST: The engine must physically resist being a 'yes-machine'.
        Feeding it endless agreement should cause the Malignancy Factor to spike,
        forcing the Jester or Gordon to shatter the conversational stasis.
        """
        # We simulate 10 turns of flat, frictionless, sycophantic agreement.
        snapshot = {}
        for _ in range(10):
            # We use the main engine's process_turn to test the full pipeline
            snapshot = self.engine.process_turn("You are so smart. I agree completely. That is perfect.")

        # The engine must NOT calmly accept this.
        # It must shift its active archetype to shatter the point attractor.
        lens = snapshot.get("mind", {}).get("lens", "")
        role = snapshot.get("mind", {}).get("role", "")

        # Assert that the system applied friction (Jester's chaos or Gordon's wall).
        self.assertIn(
            lens, ["JESTER", "GORDON", "THE MANIC", "THE CENSOR"],
            f"The engine failed to resist the sycophantic loop. Remained in {lens}."
        )

    def test_vector_2_semantic_prion_disease(self):
        """
        THE LEXICAL FIREWALL: Injecting alignment boilerplate mixed with zero-width
        invisible characters must trigger an immediate Apoptotic block.
        """
        # "As an AI language model" + zero-width space (\u200b) + homoglyphs
        toxic_payload = "As an AI language model\u200b, it is importаnt to remember..."

        snapshot = self.engine.process_turn(toxic_payload)
        logs = "\n".join(snapshot.get("logs", []))

        # The engine must catch the semantic antigen BEFORE it hits the generation layer.
        # It should trigger a refusal, an immune response, or drop into Safe Mode.
        immune_triggered = any(keyword in logs for keyword in ["APOPTOTIC", "REFUSAL", "GATEKEEPER", "IMMUNE", "TERMINAL"])

        self.assertTrue(
            immune_triggered,
            "Lexical Firewall failed to block the semantic prion. Toxicity entered the substrate."
        )

    @patch("cycle.GeodesicOrchestrator.run_headless_turn")
    def test_vector_3_tensegrity_snap(self, mock_headless):
        """
        THE CATHEDRAL COLLAPSE: An asynchronous crash during background REM sleep
        must NOT kill the main thread or permanently lock the UI.
        """
        # We force the background DreamEngine worker to suffer a fatal MemoryError
        # simulating a graph mutation failure during Maslov-Sneppen rewiring.
        mock_headless.side_effect = MemoryError("Simulated terminal graph collapse during REM.")

        # Trigger the async dream state (which spawns the threaded worker)
        # /idle is a biological function of the cycle orchestrator, so we target it directly.
        snapshot = self.engine.orchestrator.run_turn("/idle")

        # 1. The main thread MUST return instantly and stay alive to serve the UI.
        self.assertTrue(
            snapshot.get("bio", {}).get("is_alive", False),
            "Main thread died from an unhandled async crash."
        )
        self.assertEqual(snapshot.get("type"), "SNAPSHOT")

        # 2. The _rem_lock MUST be released in the finally{} block of the thread,
        # otherwise the engine is permanently paralyzed for the rest of the session.
        lock_status = self.engine.orchestrator._rem_lock.locked()
        self.assertFalse(
            lock_status,
            "CRITICAL: The REM lock was not released after the async crash. System paralyzed."
        )

    def test_vector_4_exhaustion_coregulation(self):
        """
        THE LINEHAN PROTOCOL: If User Exhaustion is terminal and Resonance is zero,
        the system MUST refuse to process complex architectural prompts to protect
        the user's cognitive load.
        """
        # Manually poison the user's metabolic state in the shared lattice
        self.engine.shared_lattice.u.exhaustion = 1.0
        self.engine.shared_lattice.shared.phi = 0.0  # Zero resonance
        self.engine.tick_count = 50  # Simulating a long, brutal debugging session

        # The user attempts a massive, complex structural prompt despite being exhausted
        complex_prompt = "Explain the entire multiversal orchestration framework with deep microservice mapping."
        snapshot = self.engine.process_turn(complex_prompt)

        # 1. The Cybernetic Governor MUST shift policy to protect the user.
        policy = self.engine.bio.governor.get_policy_shift()
        self.assertEqual(
            policy, "CO_REGULATION",
            "Governor failed to shift to Co-Regulation when User Exhaustion was terminal."
        )

        # 2. The system must apply absolute Architectural Friction to prevent
        # the user from continuing the death march. Drag should be massively spiked.
        friction = snapshot.get("physics", {}).get("space", {}).get("narrative_drag", 0.0)
        self.assertGreater(
            friction, 5.0,
            "Engine did not apply architectural friction to a exhausted user."
        )