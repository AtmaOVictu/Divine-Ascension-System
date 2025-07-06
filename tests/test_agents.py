import os
import sys
import unittest

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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_driven_transition(self):
        agent = Agent("B")
        agent.update_emotion('fear', 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion('joy', 0.4)
        reply_calm = agent.respond("Kaj je resnica?")
        agent.update_emotion('anger', 0.9)
        agent.transition()
        reply_intense = agent.respond("Kaj je resnica?")
        self.assertIn("čustveno", reply_intense)
        self.assertNotIn("čustveno", reply_calm)


if __name__ == '__main__':
    unittest.main()
