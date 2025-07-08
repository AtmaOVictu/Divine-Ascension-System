import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.memory import Memory
from divine_agents.utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    handle_complex_query,
    self_reflection,
)


class TestUtilities(unittest.TestCase):
    def test_parse_and_store(self):
        memory = Memory()
        parse_philosophical_statement("Truth is absolute and independent.", memory)
        self.assertGreater(len(memory.long_term), 0)

    def test_emotional_simulation(self):
        memory = Memory()
        result = simulate_emotional_tension({"tension_level": 1.0}, duration=2, memory=memory)
        self.assertIn("Final tension", result)
        self.assertGreater(len(memory.short_term), 0)

    def test_complex_query(self):
        memory = Memory()
        agent = Agent("A")
        response = handle_complex_query("history", agent, memory)
        self.assertIn("History length", response)

    def test_self_reflection(self):
        memory = Memory()
        memory.store_long_term({"emotion": "resolved"})
        msg = self_reflection(memory)
        self.assertIn("Improvements identified", msg)


if __name__ == '__main__':
    unittest.main()
