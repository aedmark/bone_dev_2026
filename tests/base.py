"""tests/base.py"""

import unittest
import warnings
from core import LoreManifest
from main import BoneAmanita

class BoneTestCase(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.test_config = {"PROVIDER": "mock", "boot_mode": "ADVENTURE", "MAX_STAMINA": 100.0, "MAX_HEALTH": 100.0, }
        self.engine = BoneAmanita(config=self.test_config)

    def tearDown(self):
        LoreManifest.get_instance().flush_cache()

    def generate_mock_memories(self, count=50, dim=8):
        return [(f"node_{i}", [random.uniform(-1.0, 1.0) for _ in range(dim)], {
            "concept": f"ghost_node_{i}",
            "mass": random.uniform(1.0, 10.0)
        }) for i in range(count)]