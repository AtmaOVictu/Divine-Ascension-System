import unittest
from divine_agents.agent import Agent
from divine_agents.system import DynamicAgentSystem


class TestDynamicSystem(unittest.TestCase):
    def test_run_step_transitions(self):
        system = DynamicAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system.add_agent(a1)
        system.add_agent(a2)

        lines = system.run_step()
        self.assertIn("A1 prehaja v stanje: Jaz", "\n".join(lines))
        self.assertIn("A2 prehaja v stanje: Enotnost", "\n".join(lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
