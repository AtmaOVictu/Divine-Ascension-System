import unittest
from divine_agents.agent import Agent
from divine_agents.conversation import dynamic_conversation


class TestDynamicConversation(unittest.TestCase):
    def test_conversation_transitions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = dynamic_conversation(a1, a2, [0.4, 0.9], [0.3, 0.8])
        self.assertEqual(a1.state, 'Jaz')
        self.assertEqual(a2.state, 'Enotnost')
        self.assertTrue(any('Enotnost' in line for line in lines))

    def test_conversation_dialogue(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = dynamic_conversation(a1, a2, [0.6], [0.2])
        self.assertIn('absolutna', lines[0])
        self.assertIn('relativna', lines[1])
        self.assertIn('Jaz', lines[2])


if __name__ == '__main__':
    unittest.main()
