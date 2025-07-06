import unittest
from divine_agents.agent import Agent
from divine_agents.debate import run_debate


class TestDebate(unittest.TestCase):
    def test_run_debate_transitions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = run_debate(a1, a2, rounds=2)
        self.assertEqual(a1.state, 'Enotnost')
        self.assertEqual(a2.state, 'Enotnost')
        self.assertTrue(any('Enotnost' in l for l in lines))


if __name__ == '__main__':
    unittest.main()
