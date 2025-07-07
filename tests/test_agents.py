import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_emotion_influence(self):
        agent = Agent("B")
        agent.feel("strah", 0.6)
        self.assertEqual(agent.emotion_type, "strah")
        self.assertGreater(agent.tension, 0.5)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Agent2 should reach Enotnost after feeling joy
        self.assertEqual(a2.state, "Enotnost")
        # Agent1 should transition to Jaz
        self.assertEqual(a1.state, "Jaz")
        # Dialogue lines should mention emotion influence
        self.assertTrue(any("Čutim" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
