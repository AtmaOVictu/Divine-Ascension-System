import unittest
from divine_agents import Agent, Conversation

class TestConversation(unittest.TestCase):
    def test_step_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        conv = Conversation(a1, a2)
        conv.step(0.8, 0.9)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_emotional_response(self):
        a = Agent("B")
        a.update_emotion(0.6)
        a.transition()
        self.assertIn("čustveni naboj", a.respond("Kaj je resnica?"))

if __name__ == '__main__':
    unittest.main()
