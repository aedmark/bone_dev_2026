"""tests/test_presets.py"""

from tests.base import BoneTestCase

class PresetsBoundaryTests(BoneTestCase):

    def test_absolute_zero_reconciliation(self):
        """
        The Fuller Test: Ensures the rubber band allows the system to reach absolute zero.
        Tests the fix for the phantom energy leak caused by Python's falsy 'or' evaluation.
        """
        print("\n--- PRESETS 1: Absolute Zero Reconciliation ---")

        # Ensure the physical floors are at 0.0 so we can test the resting state
        self.engine.config.PHYSICS.VOLTAGE_FLOOR = 0.0
        self.engine.config.PHYSICS.DRAG_FLOOR = 0.0

        # Feed the system an explicitly dead packet
        packet = {"voltage": 0.0, "narrative_drag": 0.0}
        reconciled = self.engine.config.reconcile_state(packet)

        # Assert the state was allowed to remain at 0.0 without triggering fallbacks
        self.assertEqual(reconciled["voltage"], 0.0, "[FAIL] Phantom energy injected! Voltage bounced off 0.0.")
        self.assertEqual(reconciled["narrative_drag"], 0.0, "[FAIL] Phantom drag injected! Drag bounced off 0.0.")

        print("  [SUCCESS] Engine successfully rested at absolute zero.")

    def test_oroboros_negative_drag_clamp(self):
        """
        The Linehan Test: Ensures a massive legacy boon applied during Genesis
        does not cause Narrative Drag to underflow below 0.0.
        """
        print("\n--- PRESETS 4: Oroboros Drag Underflow Clamping ---")
        from genesis import BoneGenesis
        from unittest.mock import patch, MagicMock

        # We mock Oroboros to return a massive drag REDUCTION (a boon of -5.0 drag)
        with patch('soul.TheOroboros.apply_legacy') as mock_oroboros:
            # Modify the dummy physics object passed to it in genesis.py
            def side_effect(dummy_phys, bio_proxy):
                dummy_phys["narrative_drag"] = -5.0
                return ["Massive Boon"]

            mock_oroboros.side_effect = side_effect

            config_dict = {"config": self.engine.config}

            # Ignite the engine
            anatomy = BoneGenesis.ignite(config_dict, lexicon_ref=MagicMock(), events_ref=MagicMock())

            # Check the awakened embryo's physics
            final_drag = getattr(anatomy["embryo"].physics, "narrative_drag", 99.0)

            self.assertGreaterEqual(final_drag, 0.0,
                                    f"[FAIL] Oroboros boon caused a mathematical underflow! Drag: {final_drag}")
            self.assertEqual(final_drag, 0.0,
                             "[FAIL] Drag did not clamp exactly to the 0.0 floor.")

        print("  [SUCCESS] Genesis smoothly clamped the legacy boon at absolute zero.")

    def test_missing_json_keys(self):
        """
        The Schur Test: Simulates a developer deleting a load-bearing key like DRAG_HALT
        from the JSON file. The system must degrade gracefully, not crash.
        """
        print("\n--- PRESETS 2: Missing Configuration Key ---")

        # Simulate missing DRAG_HALT by actively deleting it from the active config instance
        if hasattr(self.engine.config.PHYSICS, "DRAG_HALT"):
            delattr(self.engine.config.PHYSICS, "DRAG_HALT")

        try:
            # If the repair patch is active, this will silently anchor the missing key and return safely.
            # If not, this throws a fatal AttributeError and the test fails.
            errors = self.engine.config.validate_integrity()
            self.assertIsInstance(errors, list)
            print("  [SUCCESS] System survived a missing load-bearing key without an AttributeError.")
        except AttributeError as e:
            self.fail(f"[FAIL] Missing key caused a fatal boot crash: {e}")

    def test_inverted_boundaries(self):
        """
        The Meadows Test: Setting a floor higher than a ceiling should clamp
        the floor directly to the ceiling, preventing mathematically impossible negative states.
        """
        print("\n--- PRESETS 3: Inverted Boundary Clamping ---")

        # Create an inverted boundary trap where max is 0, but floor is 10
        self.engine.config.PHYSICS.VOLTAGE_MAX = 0.0
        self.engine.config.PHYSICS.VOLTAGE_FLOOR = 10.0

        # Run the integrity check
        errors = self.engine.config.validate_integrity()

        # It must clamp exactly to 0.0. If the old "ceil - 1.0" logic runs, this hits -1.0
        self.assertEqual(self.engine.config.PHYSICS.VOLTAGE_FLOOR, 0.0,
                         "[FAIL] Inverted boundary did not clamp to exactly the ceiling.")

        self.assertTrue(len(errors) > 0,  "[FAIL] System failed to log the boundary repair.")

        print("  [SUCCESS] Inverted boundaries cleanly resolved without creating negative floors.")