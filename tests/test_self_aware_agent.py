import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.self_aware_agent import SelfAwareAgent
from divine_agents.dialogue import philosophical_dialogue


class TestSelfAwareAgent(unittest.TestCase):
    def test_reflection_and_transition(self):
        agent = SelfAwareAgent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        agent.respond("Kaj je resnica?")
        self.assertTrue(any("emotion" in entry for entry in agent.history))

    def test_dialogue_responses(self):
        a1 = SelfAwareAgent("A1")
        a2 = SelfAwareAgent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
