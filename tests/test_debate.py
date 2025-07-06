import unittest
from divine_agents import Agent, apply_emotion, philosophical_debate


class TestDebate(unittest.TestCase):
    def test_apply_emotion_transition(self):
        agent = Agent('A')
        state = apply_emotion(agent, 'fear')
        self.assertEqual(state, 'Jaz')

    def test_philosophical_debate(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = philosophical_debate(a1, a2, 'anger', 'fear')
        self.assertIn('Jaz', lines[3])
        self.assertIn('Enotnost', lines[5])
        self.assertTrue(any('relativna' in line for line in lines))
        self.assertTrue(any('eno' in line for line in lines))


if __name__ == '__main__':
    unittest.main()
