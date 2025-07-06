import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.utils import numerological_value


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


class TestNumerology(unittest.TestCase):
    def test_numerological_value_scale(self):
        self.assertEqual(numerological_value(5, scale=10), 5)

    def test_agent_numerology(self):
        agent = Agent("A", tension=5, emotion=5)
        values = agent.numerology()
        self.assertEqual(values["emotion"], numerological_value(5))
        self.assertEqual(values["history"], numerological_value(1))


if __name__ == '__main__':
    unittest.main()
