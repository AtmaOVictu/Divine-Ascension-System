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

        # first exchange: should trigger Ego->Jaz for a1 and Jaz->Enotnost for a2
        step1 = manager.exchange("Kaj je resnica?", 0.6, 0.6)
        # second exchange: a1 now Jaz, should move to Enotnost
        step2 = manager.exchange("Kaj je resnica?", 0.6, 0.6)

        lines = step1 + step2

        self.assertIn("absolutna", step1[0])  # a1 was Ego at start
        self.assertIn("relativna", step2[0])  # a1 transitioned to Jaz for second step
        self.assertIn("eno", step2[1])       # a2 was Enotnost on second step

        # final states after two exchanges
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
