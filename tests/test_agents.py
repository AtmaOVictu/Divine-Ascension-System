import unittest
from divine_agents.agent import Agent, Emotion
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_tension_increases_with_emotion(self):
        agent = Agent("B")
        previous = agent.tension
        agent.update_emotion(Emotion.FEAR, 0.4)
        self.assertAlmostEqual(agent.tension, previous + 0.4)

    def test_apply_opposite(self):
        agent = Agent("C")
        agent.update_emotion(Emotion.ANGER, 1.0)
        agent.apply_opposite(0.5)
        self.assertAlmostEqual(agent.tension, 0.5)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
