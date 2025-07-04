import unittest

from divine_agents.agent import Agent
from divine_agents.system import OntologicalSystem


class TestOntologicalSystem(unittest.TestCase):
    def test_cycle_records_transition(self):
        system = OntologicalSystem()
        agent = Agent("A")
        agent.update_tension(0.8)
        system.add_agent(agent)
        system.cycle()
        self.assertEqual(len(system.history()), 1)
        self.assertEqual(system.history()[0]["to"], "Jaz")

    def test_run_multiple_cycles(self):
        system = OntologicalSystem()
        agent1 = Agent("A")
        agent1.update_tension(0.8)
        system.add_agent(agent1)
        agent2 = Agent("B", state="Jaz")
        agent2.update_tension(0.8)
        system.add_agent(agent2)
        system.run(2)
        self.assertEqual(len(system.history()), 4)


if __name__ == "__main__":
    unittest.main()
