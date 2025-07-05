import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, PHILOSOPHICAL_TRUTHS
from divine_agents.dialogue import philosophical_dialogue


class TestAgentSystem(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("T")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("E")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_philosophical_responses(self):
        for state, truth in PHILOSOPHICAL_TRUTHS.items():
            agent = Agent("A", state=state)
            self.assertIn(truth, agent.respond("Kaj je resnica?"))

    def test_dialogue_emotional_labels(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=3)
        self.assertTrue(any("Emotion:" in line for line in lines))
        # ensure at least one state transition occurs
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
