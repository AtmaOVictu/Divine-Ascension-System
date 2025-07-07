import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.krak import Krak
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

    def test_krak_high_emotion_activation(self):
        agent = Agent("K1", emotion=0.8)
        k = Krak("EmoTask", "high_emotion")
        agent.add_krak(k)
        agent.transition()
        self.assertTrue(k.completed)

    def test_krak_state_transition_activation(self):
        agent = Agent("K2")
        k = Krak("TransTask", "state_transition")
        agent.add_krak(k)
        agent.update_tension(0.8)
        agent.transition()
        self.assertTrue(k.completed)


if __name__ == '__main__':
    unittest.main()
