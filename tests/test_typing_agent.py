import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.typing_agent import TypingAgent
from divine_agents.dialogue import typing_dialogue


class TestTypingAgent(unittest.TestCase):
    def test_word_triggers_transition(self):
        agent = TypingAgent("T")
        for _ in range(8):
            agent.type_word("resnica")
        self.assertEqual(agent.state, "Jaz")

    def test_typing_dialogue(self):
        a1 = TypingAgent("A1")
        a2 = TypingAgent("A2", state="Jaz")
        lines = typing_dialogue(a1, a2, ["resnica", "harmonija"])
        self.assertTrue(any("Jaz" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
