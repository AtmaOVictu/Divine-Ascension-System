import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.phases import create_res_phases

class TestRESPhases(unittest.TestCase):
    def test_create_res_phases(self):
        phases = create_res_phases()
        self.assertEqual(len(phases), 103)
        self.assertEqual(phases[0].label, "RES000")
        labels = [p.label for p in phases]
        self.assertIn("RES100", labels)

if __name__ == "__main__":
    unittest.main()
