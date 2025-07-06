import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate
from divine_agents.emotion import Emotion


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

    def test_apply_emotion(self):
        agent = Agent("A")
        emotion = Emotion("jeza", 0.4, 0.3, 0.1, 0.2)
        agent.apply_emotion(emotion)
        self.assertGreaterEqual(agent.tension, 1.0)

    def test_philosophical_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        dialogue = philosophical_debate(a1, a2, turns=3)
        self.assertTrue(any("Enotnost" in line for line in dialogue))


if __name__ == '__main__':
    unittest.main()
