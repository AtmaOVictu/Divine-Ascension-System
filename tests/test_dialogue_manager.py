import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import DialogueManager


class TestDialogueManager(unittest.TestCase):
    def test_full_conversation_cycle(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        manager = DialogueManager(a1, a2)

        questions = ["Kaj je resnica?", "Kaj je resnica?"]
        emotions = [0.6, 0.6]

        lines = manager.start_dialogue(questions, emotions, emotions)

        self.assertIn("absolutna", lines[0])  # a1 was Ego at start
        self.assertIn("relativna", lines[2])  # a1 transitioned to Jaz by second exchange
        self.assertIn("eno", lines[3])       # a2 reached Enotnost

        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")

    def test_monologue(self):
        agent = Agent("Solo")
        manager = DialogueManager(agent)

        lines = manager.start_monologue(["Kaj je resnica?"], [0.6])
        self.assertIn("Solo", lines[0])
        self.assertEqual(agent.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
