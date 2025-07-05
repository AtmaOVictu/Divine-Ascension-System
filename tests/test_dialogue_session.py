import unittest
from divine_agents import Agent, DialogueSession


class TestDialogueSession(unittest.TestCase):
    def test_session_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        session = DialogueSession(a1, a2)
        # emotions trigger transitions in both agents
        session.run([0.8], [0.6])
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Čutim", reply)


if __name__ == '__main__':
    unittest.main()
