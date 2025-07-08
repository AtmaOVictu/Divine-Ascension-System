import os, sys; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.utils import (
    Memory,
    parse_philosophical_statement,
    simulate_emotional_tension,
    handle_complex_query,
    self_reflection,
)


class TestUtils(unittest.TestCase):
    def test_parse_philosophical_statement(self):
        mem = Memory()
        result = parse_philosophical_statement("Truth is unity and relation", mem)
        self.assertIn("Truth", result)
        self.assertEqual(len(mem.long_term), 1)

    def test_simulate_emotional_tension(self):
        mem = Memory()
        tension = simulate_emotional_tension({"tension_level": 1.0}, 2, mem)
        self.assertLess(tension, 1.0)
        self.assertEqual(len(mem.short_term), 1)

    def test_handle_complex_query(self):
        mem = Memory()
        out = handle_complex_query("resolve paradox", {"tension_level": 0.5}, mem)
        self.assertIn("Paradox", out)

    def test_self_reflection(self):
        mem = Memory()
        parse_philosophical_statement("A is A", mem)
        msg = self_reflection(mem)
        self.assertIn("Entries reviewed", msg)


if __name__ == "__main__":
    unittest.main()
