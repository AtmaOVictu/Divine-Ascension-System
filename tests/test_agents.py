import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_automatic_transition_on_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_history_recording(self):
        agent = Agent("H")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any(a1.emotion_label() in line for line in lines))

    def test_configurable_thresholds(self):
        agent = Agent("C", tension_threshold=0.2, emotion_threshold=0.2)
        agent.update_emotion(0.21)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")



if __name__ == '__main__':
    unittest.main()

