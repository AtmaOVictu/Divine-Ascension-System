import unittest

from divine_agents.agent import Agent
from divine_agents.iglo_agent import IgloAgent


class TestIgloAgent(unittest.TestCase):
    def test_sequential_and_parallel_execution(self):
        def block_1(results):
            results['data'] = 'prep'
            return 'prep'

        def block_2(results):
            return f"analysis-{results['data']}"

        def block_3(results):
            return 'report'

        iglo = IgloAgent()
        iglo.execute([block_1, block_2], [block_3])
        self.assertEqual(iglo.results['block_1'], 'prep')
        self.assertEqual(iglo.results['block_2'], 'analysis-prep')
        self.assertEqual(iglo.results['block_3'], 'report')

    def test_agent_transition_with_iglo(self):
        agent = Agent('X')

        def update_agent(results):
            agent.update_emotion(0.8)
            return agent.transition()

        iglo = IgloAgent()
        iglo.execute([update_agent], [])
        self.assertEqual(agent.state, 'Jaz')


if __name__ == '__main__':
    unittest.main()
