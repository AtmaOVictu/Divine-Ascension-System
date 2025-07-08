import unittest
from divine_agents import Agent, AgentNetwork, SharedMemory, group_dialogue


class TestAgentNetwork(unittest.TestCase):
    def test_evolve_agents(self):
        mem = SharedMemory()
        network = AgentNetwork(mem)
        a1 = Agent("A1")
        a2 = Agent("A2")
        network.add_agent(a1)
        network.add_agent(a2)
        network.evolve()
        # After evolve, emotion updated causing transition
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)

    def test_group_dialogue(self):
        agents = [Agent("A1"), Agent("A2", state="Jaz")]
        lines = group_dialogue(agents)
        self.assertEqual(len(lines), 4)
        self.assertTrue(any("po refleksiji" in l for l in lines))


if __name__ == "__main__":
    unittest.main()
