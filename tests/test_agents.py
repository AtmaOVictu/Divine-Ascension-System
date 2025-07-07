import os
import sys
import unittest

# Ensure the package is importable when tests are run directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, Emotion, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(Emotion.FEAR, 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_in_response(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion(Emotion.JOY, 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)
        self.assertIn("relativna", reply)

    def test_dialogue_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After transitions one of the agents should be in Jaz or Enotnost
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines[2:]))


if __name__ == "__main__":
    unittest.main()
