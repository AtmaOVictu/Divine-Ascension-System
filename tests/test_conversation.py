import unittest
from divine_agents.agent import Agent
from divine_agents.conversation import Conversation


class TestConversation(unittest.TestCase):
    def test_run_conversation_transitions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        convo = Conversation(a1, a2)
        transcript = convo.run([(0.8, 0.2), (0.1, 0.6)])

        # Both agents should end in Enotnost after accumulating tension
        self.assertEqual(a1.state, 'Enotnost')
        self.assertEqual(a2.state, 'Enotnost')
        # Transcript should reflect philosophical positions
        joined = '\n'.join(transcript)
        self.assertIn('relativna', joined)
        self.assertIn('eno', joined)


if __name__ == '__main__':
    unittest.main()
