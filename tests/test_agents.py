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

    def test_transition_emotion_only(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_history_records_states(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.9, emotion2=0.7)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_varied_emotions(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.9, emotion2=0.4)
        self.assertIn("B1 prehaja v stanje: Jaz", lines)
        self.assertIn("B2 prehaja v stanje: Jaz", lines)


if __name__ == '__main__':
    unittest.main()
