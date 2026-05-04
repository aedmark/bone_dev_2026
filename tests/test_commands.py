"""
tests/test_commands.py

The Executive Torture Chamber.
Validates that the CLI router correctly enforces metabolic limits, architectural bounds,
and syntactic resilience when handling human input.
"""

from unittest.mock import MagicMock
from tests.base import BoneTestCase
from main import BoneAmanita
from constants import Prisma
from mechanics.commands import CommandProcessor, ResourceTax, CommandStateInterface

class CommandSystemTests(BoneTestCase):

    def test_meadows_metabolic_exhaustion_rejection(self):
        """
        The Tax Collector must completely reject high-cost commands if the system
        is starving, and it must PREVENT partial deductions from bankrupting the ATP pool.
        """
        engine = BoneAmanita({})
        # Force the engine into a starving state (5 ATP).
        # /podcast requires 20 ATP.
        engine.set_atp(5.0)
        processor = CommandProcessor(engine, Prisma)

        initial_atp = engine.get_metrics().get("atp", 0.0)

        # Execute the high-cost command
        processor.execute("/podcast The Nature of Technical Debt")

        final_atp = engine.get_metrics().get("atp", 0.0)

        # Assertion 1: The engine did not execute the command and did not deduct partial ATP.
        self.assertEqual(initial_atp, final_atp)
        self.assertEqual(final_atp, 5.0)

    def test_fuller_resource_clamping_integrity(self):
        """
        The Command Interface must absolutely respect the biological ceiling and floor.
        You cannot have negative stamina, nor can you over-heal past the config max.
        """
        engine = BoneAmanita({})
        processor = CommandProcessor(engine, Prisma)

        # Test 1: Massive Drain (The Floor)
        processor.interface.modify_resource("stamina", -500.0)
        self.assertEqual(processor.interface.get_resource("stamina"), 0.0, "Stamina failed to clamp at absolute zero.")

        # Test 2: Massive Over-heal (The Ceiling)
        max_stamina = engine.config.MAX_STAMINA
        processor.interface.modify_resource("stamina", 5000.0)
        self.assertEqual(processor.interface.get_resource("stamina"), max_stamina, "Stamina breached the architectural ceiling.")

    def test_gordon_reality_stack_lockout(self):
        """
        If the system is in a deep Reality Layer that forbids human intervention
        (e.g., a fatal crash or deep REM cycle), the processor must bounce the command immediately.
        """
        engine = BoneAmanita({})
        processor = CommandProcessor(engine, Prisma)

        # Mock a deep reality layer that explicitly forbids commands
        class MockRealityStack:
            current_depth = 4
            def get_grammar_rules(self):
                return {"allow_commands": False}

        engine.reality_stack = MockRealityStack()

        # /trauma is a dev command that forcefully drops health to 20.
        engine.health = 100.0
        processor.execute("/trauma")

        # Assertion: Because the reality stack locked the UI, the command should have been ignored.
        self.assertEqual(engine.health, 100.0, "Gordon failed to hold the wall. Command bypassed Reality Stack lock.")

    def test_pinker_syntactic_resilience(self):
        """
        The Command Registry must survive mangled spacing, missing arguments,
        and entirely fabricated slash commands without throwing Python exceptions.
        """
        engine = BoneAmanita({})
        processor = CommandProcessor(engine, Prisma)

        try:
            # 1. Unknown Command
            processor.execute("/hallucinate")

            # 2. Command expecting arguments, but given none
            processor.execute("/mode")
            processor.execute("/truth")

            # 3. Extreme whitespace formatting
            processor.execute("/use    ITEM    NAME  ")

            # If we reach here without a KeyError, IndexError, or ValueError, the registry is structurally sound.
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Syntactic noise shattered the command processor: {e}")

    def test_jester_shuffle_resets_drag(self):
        """
        Validates that the Jester's Gambit (/shuffle) successfully executes,
        taxes the system, and explicitly zeroes out accumulated narrative drag.
        """
        engine = BoneAmanita({})
        engine.set_atp(100.0)

        # Mock physics state with high drag
        class MockPhys:
            narrative_drag = 8.5
        engine.phys = MockPhys()

        processor = CommandProcessor(engine, Prisma)

        initial_atp = engine.get_metrics().get("atp", 0.0)

        # Execute the shuffle
        processor.execute("/shuffle")

        # Assertion 1: Narrative Drag must be physically reset to 0.
        self.assertEqual(engine.phys.narrative_drag, 0.0, "Jester failed to clear the narrative gravity well.")

        # Assertion 2: The system must have paid the ATP cost for the gambit.
        final_atp = engine.get_metrics().get("atp", 0.0)
        self.assertTrue(final_atp < initial_atp, "The Shuffle occurred without levying the ATP tax.")