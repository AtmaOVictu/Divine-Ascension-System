import unittest
from divine_agents import simple_numpy as np

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotion import Emotion
from divine_agents.karma import Karma
from divine_agents.helper import AgentHelper


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


class TestEmotionsKarma(unittest.TestCase):
    def test_emotion_transition(self):
        e = Emotion(despair=0.9)
        e.transition()
        self.assertGreater(e.hope, 0.0)
        self.assertLess(e.despair, 0.9)

    def test_karma_tracking(self):
        e = Emotion(joy=0.9)
        k = Karma()
        state = np.zeros((2, 2))
        k.update(e, state)
        self.assertEqual(len(k.track_karma_over_time()), 1)

    def test_emotional_contagion(self):
        helper = AgentHelper(2)
        helper.emotions[0] = 1.0
        influence = np.array([[0.0, 0.5], [0.5, 0.0]])
        updated = helper.update_emotions(influence)
        self.assertNotEqual(updated[1], 0.0)


if __name__ == '__main__':
    unittest.main()
