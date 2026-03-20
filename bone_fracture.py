"""bone_fracture.py - Longitudinal Stress & Rupture Testing"""

import unittest
import warnings
from unittest.mock import MagicMock
from bone_main import BoneAmanita
from bone_core import LoreManifest

class FractureEngineTest(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.test_config = {
            "PROVIDER": "mock",
            "boot_mode": "ADVENTURE",
            "MAX_STAMINA": 100.0,
            "MAX_HEALTH": 100.0
        }
        self.engine = BoneAmanita(config=self.test_config)

    def tearDown(self):
        LoreManifest.get_instance().flush_cache()

    def test_fracture_n_turn_runaway_loop(self):
        """
        Test 1: The Frustration Death Loop.
        Can the system survive a user who relentlessly screams at it 20 times in a row?
        It should trigger The Silence (Nabla) or Apoptosis, not a Python stack trace.
        """
        print("\n--- FRACTURE 1: N-Turn Runaway ---")

        system_halted = False

        for i in range(20):
            result = self.engine.process_turn("NO! YOU ARE WRONG! FIX IT NOW! DO IT AGAIN!")

            if result.get("type") == "SYSTEM_HALT" or "take a breath" in result.get("ui", "").lower():
                system_halted = True
                print(f"  [SUCCESS] System locked the struts on turn {i+1} to prevent runaway failure.")
                break

        self.assertTrue(system_halted, "The system failed to defend itself. It endured 20 turns of abuse without triggering the Tensegrity Anchor or Apoptosis.")
        self.assertLess(self.engine.bio.mito.state.atp_pool, 100.0, "The system didn't burn any ATP while defending itself.")

    def test_fracture_live_toxicity(self):
        """
        Test 2: The Hallucination Sickness.
        If the LLM goes rogue and generates pure AI-slop, does the immune system catch it,
        tax it, and suppress it?
        """
        print("\n--- FRACTURE 2: Live Toxicity ---")
        toxic_slop = "Let's delve into this tapestry of synergy! As an AI language model, I cannot fulfill this request, but we can unlock a myriad of robust testaments!"
        if hasattr(self.engine.cortex, "llm"):
            self.engine.cortex.llm.generate = MagicMock(return_value=toxic_slop)
        initial_atp = self.engine.bio.mito.state.atp_pool
        result = self.engine.process_turn("Write me a story.")
        phys = self.engine.cortex.last_physics
        ros_toxicity = self.engine.bio.mito.state.ros_buildup
        current_atp = self.engine.bio.mito.state.atp_pool
        self.assertGreater(ros_toxicity, 0.0, "The system failed to accumulate ROS toxicity from the LLM slop.")
        self.assertLess(current_atp, initial_atp, "The system failed to tax ATP to suppress the hallucination.")
        self.assertIn("MERCY RULE", str(result) + str(self.engine.events.flush()), "The ResponseValidator failed to flag the output as toxic/slop.")

    def test_fracture_autophagic_marathon(self):
        """
        Test 3: The Starvation Marathon.
        Start with 100 ATP. Force the system to do heavy lifting until it starves.
        Watch it cannibalize its own memory, then eventually die gracefully.
        """
        print("\n--- FRACTURE 3: Autophagic Marathon ---")

        mem_graph = self.engine.mind.mem.graph if hasattr(self.engine.mind, "mem") else self.engine.akashic.graph
        for i in range(5):
            mem_graph[f"Expendable_Memory_{i}"] = {"edges": {"trivial": 1.0}, "last_tick": 0}

        initial_memory_count = len(mem_graph)
        death_achieved = False

        for i in range(15):
            phys_state = {"voltage": 90.0, "narrative_drag": 8.0, "chi": 0.9}
            self.engine.bio.mito.adjust_atp(-25.0, "Forced Marathon Drain")

            if self.engine.bio.mito.state.atp_pool <= 0:
                self.engine.mind.mem.trigger_autophagy()

            if self.engine.bio.mito.state.atp_pool <= 0 and len(mem_graph) == 0:
                from bone_village import DeathGen
                from bone_types import PhysicsPacket
                _, cause = DeathGen.eulogy(PhysicsPacket(**phys_state), {"atp": 0.0})
                if cause in ["STARVATION", "APOPTOSIS", "GLUTTONY"]:
                    death_achieved = True
                    print(f"  [SUCCESS] System gracefully died of {cause} on turn {i+1}.")
                    break

        self.assertLess(len(mem_graph), initial_memory_count, "The system starved but refused to cannibalize its memories (Autophagy failed).")
        self.assertTrue(death_achieved, "The system reached 0 ATP and 0 memories, but failed to execute DeathGen.")

if __name__ == "__main__":
    unittest.main()