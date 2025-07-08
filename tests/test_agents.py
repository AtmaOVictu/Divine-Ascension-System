import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
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

    def test_emotional_recovery(self):
        em = Emotion(despair=0.9)
        em.transition()
        self.assertGreater(em.hope, 0)
        self.assertLess(em.despair, 0.9)

    def test_karma_tracking(self):
        agent = Agent("A")
        for _ in range(3):
            agent.update_emotion(0.6)
        self.assertEqual(len(agent.karma.track_karma_over_time()), 3)

    def test_contagion(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        a2.update_emotion(0.6)
        a1.contagion([a2])
        self.assertNotEqual(a1.emotion, 0.0)


if __name__ == '__main__':
    unittest.main()
