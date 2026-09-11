import unittest
import os
import sys

# Ensure the package is importable when tests are run directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, exchanges=2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(len(lines), 2 + 4 * 2)

    def test_history_accumulation(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_emotion_clamping(self):
        agent = Agent("A")
        agent.update_emotion(2.0)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)


if __name__ == '__main__':
    unittest.main()
