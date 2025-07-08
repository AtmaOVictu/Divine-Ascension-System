import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, compliant_dialogue
from divine_agents.compliance import DataCompliantRecursiveAgent


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestDataCompliance(unittest.TestCase):
    def test_data_logging(self):
        agent = DataCompliantRecursiveAgent("C")
        agent.adapt("input")
        agent.reflect()
        self.assertGreaterEqual(len(agent.data_usage_log), 2)

    def test_compliant_dialogue(self):
        a1 = DataCompliantRecursiveAgent("A1")
        a2 = DataCompliantRecursiveAgent("A2", state="Jaz")
        lines = compliant_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
