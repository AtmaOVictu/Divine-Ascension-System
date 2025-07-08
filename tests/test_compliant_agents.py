import unittest

from divine_agents.compliant_agent import DataCompliantRecursiveAgent
from divine_agents.dialogue import compliant_philosophical_dialogue


class TestDataCompliantRecursiveAgent(unittest.TestCase):
    def test_logging_and_transition(self):
        agent = DataCompliantRecursiveAgent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertTrue(len(agent.history) >= 2)

    def test_data_logging(self):
        agent = DataCompliantRecursiveAgent("A")
        agent.adapt("input")
        self.assertGreater(len(agent.usage_log), 0)

    def test_compliant_dialogue(self):
        a1 = DataCompliantRecursiveAgent("A1")
        a2 = DataCompliantRecursiveAgent("A2", state="Jaz")
        lines = compliant_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Resnica" in line for line in lines))
        self.assertGreater(len(a1.usage_log), 0)
        self.assertGreater(len(a2.usage_log), 0)


if __name__ == '__main__':
    unittest.main()
