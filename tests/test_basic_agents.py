import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.basic_agents import BitAgent, AlphabetAgent


class TestBasicAgents(unittest.TestCase):
    def test_bit_agent_transition(self):
        agent = BitAgent("Bit01", 0)
        self.assertEqual(agent.transition(), 1)
        self.assertEqual(agent.transition(), 0)

    def test_alphabet_agent_transition(self):
        agent = AlphabetAgent("Alpha01", "A")
        self.assertEqual(agent.transition(), "B")
        self.assertEqual(agent.transition(), "C")


if __name__ == "__main__":
    unittest.main()
