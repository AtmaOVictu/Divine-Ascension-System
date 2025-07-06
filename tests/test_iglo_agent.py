import unittest
from divine_agents.iglo_agent import IgloAgent


# Example blocks used for testing

def block_a(results):
    results['a'] = 'A'
    return 'A done'

def block_b(results):
    results['b'] = results.get('a', '') + 'B'
    return 'B done'

def block_c(results):
    results['c'] = 'C'
    return 'C done'


class TestIgloAgent(unittest.TestCase):
    def test_sequence(self):
        agent = IgloAgent()
        agent.execute_in_sequence([block_a, block_b])
        self.assertEqual(agent.results['a'], 'A')
        self.assertEqual(agent.results['b'], 'AB')

    def test_parallel(self):
        agent = IgloAgent()
        agent.execute_in_parallel([block_a, block_c])
        self.assertIn('a', agent.results)
        self.assertIn('c', agent.results)
        self.assertEqual(agent.results['a'], 'A')
        self.assertEqual(agent.results['c'], 'C')

    def test_execute(self):
        agent = IgloAgent()
        results = agent.execute([block_a], [block_b, block_c])
        # block_b depends on block_a's result
        self.assertEqual(results['b'], 'AB')
        self.assertIn('c', results)


if __name__ == '__main__':
    unittest.main()
