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

        # second transition via emotion
        agent.update_emotion(0.9, "fear")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.3)
        agent.update_emotion(0.2, "joy")
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_numerological_value(self):
        self.assertEqual(numerological_value(0.5, scale=1), 5.0)
        self.assertEqual(numerological_value(2, scale=2), 10.0)


if __name__ == '__main__':
    unittest.main()
