import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import VeraVoljaLjubAgent, philosophical_dialogue


class TestCompositeAgent(unittest.TestCase):
    def test_process_transitions(self):
        agent = VeraVoljaLjubAgent('A')
        logs = agent.run_process()
        self.assertEqual(agent.state, 'Enotnost')
        self.assertEqual(agent.vera.state, 3)
        self.assertEqual(agent.volja.state, 3)
        self.assertEqual(agent.ljubezen.state, 3)
        self.assertTrue(any('harmonija' in log.lower() for log in logs))

    def test_dialogue_with_emotion(self):
        a1 = VeraVoljaLjubAgent('A1')
        a2 = VeraVoljaLjubAgent('A2', state='Jaz')
        convo = philosophical_dialogue(a1, a2)
        self.assertTrue(any('Enotnost' in line for line in convo))
        self.assertTrue(any('Resnica' in line for line in convo))


if __name__ == '__main__':
    unittest.main()
