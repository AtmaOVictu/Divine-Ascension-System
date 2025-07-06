import unittest

from divine_agents.agent import Agent
from divine_agents.symbolic import SymbolicAgent, SymbolicSubAgent
from divine_agents.dialogue import philosophical_dialogue


class TestSymbolicAgent(unittest.TestCase):
    def test_subagent_creation(self):
        symbols = ['A', 'B']
        sa = SymbolicAgent('S', symbols)
        self.assertEqual(len(sa.sub_agents), 2)
        self.assertIsInstance(sa.sub_agents['A'], SymbolicSubAgent)

    def test_operate_returns_messages(self):
        sa = SymbolicAgent('S', ['X'])
        results = sa.operate()
        self.assertIn("Podagent za simbol 'X'", results[0])


class TestEmotionTransitions(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = Agent('E')
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, 'Jaz')

    def test_dialogue_contains_states(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = philosophical_dialogue(a1, a2)
        joined = "\n".join(lines)
        self.assertIn('Jaz', joined)
        self.assertIn('Enotnost', joined)


if __name__ == '__main__':
    unittest.main()
