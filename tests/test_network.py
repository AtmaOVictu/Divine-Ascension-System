import unittest
from divine_agents.agent import Agent
from divine_agents.network import AgentNetwork

class TestAgentNetwork(unittest.TestCase):
    def test_evolution(self):
        net = AgentNetwork()
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        net.add_agent(a1)
        net.add_agent(a2)

        a1.update_tension(0.7)
        a2.update_emotion(0.6)
        net.evolve_agents()

        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        # at least one agent should have transitioned due to learning
        self.assertTrue(a1.state != 'Ego' or a2.state != 'Jaz')

if __name__ == '__main__':
    unittest.main()

