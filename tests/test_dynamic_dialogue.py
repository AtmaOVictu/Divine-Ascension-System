import os
import sys
import unittest

# Ensure project root is importable when running from tests directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_philosophical_dialogue


class TestDynamicDialogue(unittest.TestCase):
    def test_emotion_triggers_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.6, label="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("fear", agent.respond("Kaj?"))

    def test_dynamic_dialogue_results(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

