import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.special_agents import LogicAgent, ConfirmationAgent, DeconfirmationAgent
from divine_agents.system import MultiAgentSystem


class TestAdvancedAgents(unittest.TestCase):
    def test_logic_agent_evaluation(self):
        agent = LogicAgent("Logic")
        agent.add_fact("earth_is_round", True)
        self.assertTrue(agent.evaluate("earth_is_round"))

    def test_confirmation_agent(self):
        agent = ConfirmationAgent("Confirm")
        agent.confirm_fact("earth_is_round", True)
        self.assertTrue(agent.verify_decision("earth_is_round"))

    def test_deconfirmation_agent(self):
        agent = DeconfirmationAgent("Doubt")
        agent.challenge_fact("earth_is_round")
        result = agent.deconfirm_fact("earth_is_round")
        self.assertIn("successful", result)

    def test_multi_agent_system_interaction(self):
        l = LogicAgent("L")
        l.add_fact("earth_is_round", True)
        c = ConfirmationAgent("C")
        c.confirm_fact("earth_is_round", True)
        d = DeconfirmationAgent("D")
        mas = MultiAgentSystem([l, c, d])
        mas.start_interaction()
        states = mas.check_agents_status()
        self.assertTrue(all("Jaz" in line or "Enotnost" in line for line in states))


if __name__ == '__main__':
    unittest.main()
