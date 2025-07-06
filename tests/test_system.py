import unittest
from divine_agents.agent import Agent
from divine_agents.system import DynamicAgentSystem


class TestDynamicAgentSystem(unittest.TestCase):
    def test_simulation_transitions(self):
        system = DynamicAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system.add_agent(a1)
        system.add_agent(a2)
        transcript = system.run_simulation()
        # ensure each agent transitions once
        self.assertIn("Jaz", transcript[1])  # A1 should transition to Jaz
        self.assertIn("Enotnost", transcript[4])  # A2 should transition to Enotnost


if __name__ == "__main__":
    unittest.main()
