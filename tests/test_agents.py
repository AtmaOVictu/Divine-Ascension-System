import unittest
import numpy as np
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.dynamics import Karma, track_emotional_trends
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

    def test_karma_update(self):
        emotion = Emotion(joy=0.9)
        karma = Karma()
        state = np.zeros((5, 5))
        value = karma.update(emotion, state)
        self.assertGreater(value, 0)

    def test_track_emotional_trends(self):
        emotions_series = [Emotion(joy=0.5, hope=0.6), Emotion(anger=0.7)]
        trends = track_emotional_trends(emotions_series, iterations=5)
        self.assertEqual(len(trends['karma']), 2)
        self.assertEqual(len(trends['karma'][0]), 5)


if __name__ == '__main__':
    unittest.main()
