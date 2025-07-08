import unittest
import numpy as np

from divine_agents import (
    Agent,
    Emotion,
    Karma,
    Agent1Helper,
    philosophical_dialogue,
    emotional_dialogue,
)


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

    def test_emotion_recovery(self):
        e = Emotion(despair=0.9)
        e.transition()
        self.assertGreater(e.hope, 0)
        self.assertLess(e.despair, 0.9)

    def test_karma_update(self):
        k = Karma()
        e = Emotion(joy=0.9)
        k.update(e, np.random.rand(2, 2))
        self.assertGreater(k.karma_value, 0)
        self.assertEqual(len(k.karma_history), 1)

    def test_emotional_contagion(self):
        helper = Agent1Helper(2)
        helper.emotions = [1.0, -1.0]
        influence = [[0, 1], [1, 0]]
        helper.update_emotions(influence)
        self.assertTrue(all(e <= 1 for e in helper.emotions))
        self.assertTrue(any(e != t for e, t in zip(helper.emotions, [1.0, -1.0])))

    def test_emotional_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        e1 = Emotion(fear=0.6)
        e2 = Emotion(anger=0.7)
        lines = emotional_dialogue(a1, a2, e1, e2)
        self.assertTrue(any("Karma" in line for line in lines))
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == "__main__":
    unittest.main()
