import unittest
from divine_agents import Agent, DynamicAgentSystem


class TestDynamicAgentSystem(unittest.TestCase):
    def test_simulation_transitions(self):
        system = DynamicAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system.add_agent(a1)
        system.add_agent(a2)

        lines = system.run_simulation("Kaj je resnica?")
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertEqual(len(lines), 4)


if __name__ == "__main__":
    unittest.main()
