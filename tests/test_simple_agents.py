import unittest
from divine_agents.simple_agents import BitAgent, AlphabetAgent


class TestSimpleAgents(unittest.TestCase):
    def test_bit_agent_toggle(self):
        agent = BitAgent("b1", 0)
        self.assertEqual(agent.transition(), 1)
        self.assertEqual(agent.transition(), 0)

    def test_alphabet_agent_cycle(self):
        agent = AlphabetAgent("a1", "A")
        self.assertEqual(agent.transition(), "B")
        for _ in range(24):
            agent.transition()
        self.assertEqual(agent.transition(), "A")


if __name__ == "__main__":
    unittest.main()
