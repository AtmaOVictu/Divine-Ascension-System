import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from divine_agents.agent import Agent, Emotion
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

    def test_emotion_dataclass(self):
        agent = Agent("B")
        agent.update_emotion(
            Emotion(
                energy=0.6,
                motivation=0.6,
                feeling=0.6,
                tension=0.6,
                intensity=0.6,
                potential=0.6,
            )
        )
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("C")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("intenzivna", reply)


if __name__ == '__main__':
    unittest.main()
