import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.8, emotion_type="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("emocija", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect at least one transition to Enotnost in conversation
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertGreaterEqual(len(lines), 4)


if __name__ == '__main__':
    unittest.main()
