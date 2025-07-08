import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotion import Emotion
from divine_agents.karma import Karma
from divine_agents.visualization import track_emotional_trends


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

    def test_emotional_interaction(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        a2.update_emotion(0.6)
        a1.interact([a2], influence_factor=0.5)
        self.assertGreater(a1.emotion, 0)

    def test_karma_update(self):
        e = Emotion(anger=0.9)
        karma = Karma()
        value = karma.update(e, [[0.0, 0.0], [0.0, 0.0]])
        self.assertLess(value, 0)

    def test_track_emotional_trends(self):
        series = [Emotion(joy=0.5), Emotion(anger=0.6)]
        trends = track_emotional_trends(series, iterations=5)
        self.assertIn('karma', trends)


if __name__ == '__main__':
    unittest.main()
