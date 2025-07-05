import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.conversation import Conversation


class TestConversation(unittest.TestCase):
    def test_conversation_full_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        conv = Conversation(a1, a2)
        conv.run("Kaj je resnica?", steps=3)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")

    def test_dialogue_lines_content(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        conv = Conversation(a1, a2)
        lines = conv.run("Kaj je resnica?", steps=1)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
