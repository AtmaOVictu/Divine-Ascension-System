import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.memory import Memory
from divine_agents.utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
)


class TestUtils(unittest.TestCase):
    def test_parse_philosophical_statement(self):
        mem = Memory()
        parse_philosophical_statement("Truth is one", mem)
        self.assertEqual(len(mem.long_term), 1)

    def test_simulate_emotional_tension(self):
        mem = Memory()
        result = simulate_emotional_tension({"tension_level": 1.0}, 2, mem)
        self.assertIn("Final tension", result)
        self.assertAlmostEqual(mem.short_term[0]["final_tension"], 0.9, places=2)


if __name__ == "__main__":
    unittest.main()

