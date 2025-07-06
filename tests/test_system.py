import unittest
from divine_agents.agent import Agent
from divine_agents.system import DynamicAgentSystem


class TestDynamicAgentSystem(unittest.TestCase):
    def test_agent_movement_between_modules(self):
        system = DynamicAgentSystem()
        a1 = Agent('A1')
        system.add_agent(a1)
        # Increase emotion to trigger transition
        a1.update_emotion(0.8)
        system.step()
        summary = system.summary()
        self.assertNotIn('A1', summary['Ego'])
        self.assertIn('A1', summary['Jaz'])


if __name__ == '__main__':
    unittest.main()
