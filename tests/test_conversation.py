import unittest
from divine_agents.agent import Agent
from divine_agents.conversation import engage_agents


class TestConversation(unittest.TestCase):
    def test_engagement_transitions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = engage_agents(a1, a2, rounds=2)
        # ensure at least one agent reaches new state
        self.assertTrue(any('prehaja v stanje' in line for line in lines))
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
