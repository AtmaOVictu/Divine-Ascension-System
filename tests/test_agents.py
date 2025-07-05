import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.utils import logistic_growth


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

    def test_logistic_growth_transition(self):
        agent = Agent("L")
        state = agent.apply_logistic_tension(2.0)
        self.assertEqual(state, "Jaz")

    def test_logistic_growth_value(self):
        value = logistic_growth(2.0)
        self.assertGreater(value, 0.7)


if __name__ == '__main__':
    unittest.main()
