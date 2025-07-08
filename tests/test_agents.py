import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotion import Emotion
from divine_agents.tracker import track_emotional_trends


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(anger=0.8)
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

    def test_emotional_trends(self):
        emotions = [Emotion(joy=0.5, hope=0.6)]
        trends = track_emotional_trends(emotions, iterations=3)
        self.assertIn('karma', trends)
        self.assertEqual(len(trends['karma'][0]), 3)


if __name__ == '__main__':
    unittest.main()
