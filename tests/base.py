"""tests/base.py"""

import unittest
import warnings
from core import LoreManifest
from main import BoneAmanita
from constants import Prisma

class BoneTestCase(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.test_config = {"PROVIDER": "ollama", "boot_mode": "DEEP", "MAX_STAMINA": 100.0, "MAX_HEALTH": 100.0, }
        print(f"\n{Prisma.CYN}>>> STARTING TEST: {self.id()}{Prisma.RST}")
        self.engine = BoneAmanita(config=self.test_config)

    def tearDown(self):
        print(f"{Prisma.GRN}<<< COMPLETED TEST: {self.id()}{Prisma.RST}\n")
        LoreManifest.get_instance().flush_cache()