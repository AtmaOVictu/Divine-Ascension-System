import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotion import logistic_emotion


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
        lines = philosophical_dialogue(a1, a2, time=1.0)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestEmotionFunction(unittest.TestCase):
    def test_logistic_range(self):
        value = logistic_emotion(1.0, k=1.0, c=0.0)
        self.assertGreater(value, 0.0)
        self.assertLess(value, 1.0)


if __name__ == '__main__':
    unittest.main()
