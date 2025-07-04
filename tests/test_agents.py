import os
import sys
import unittest

# Ensure package can be imported when PYTHONPATH is not set
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, EmotionType
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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("\u010dustvo" in line for line in lines))

    def test_emotion_update(self):
        agent = Agent("B")
        agent.update_emotion(0.9, EmotionType.ANGER)
        self.assertEqual(agent.emotion_type, EmotionType.ANGER)
        self.assertGreater(agent.tension, 0.8)


if __name__ == '__main__':
    unittest.main()
