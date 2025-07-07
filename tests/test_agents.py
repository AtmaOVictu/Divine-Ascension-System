import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, segmented_dialogue


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

    def test_segmented_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = segmented_dialogue(a1, a2, cycles=3)
        self.assertTrue(any("Jaz" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_triggers_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertIn(state, ("Jaz", "Enotnost"))

    def test_history_records_transitions(self):
        a1 = Agent("A1")
        segmented_dialogue(a1, Agent("B"), cycles=3)
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a1.history)


if __name__ == '__main__':
    unittest.main()
