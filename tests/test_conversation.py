import unittest
from divine_agents.agent import Agent
from divine_agents.conversation import Conversation


class TestConversation(unittest.TestCase):
    def test_conversation_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        conv = Conversation(a1, a2)
        conv.run(rounds=2, emotions1=[0.8, 0.2], emotions2=[0.6, 0.1])
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Resnica" in line for line in conv.history))


if __name__ == "__main__":
    unittest.main()
