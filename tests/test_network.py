import unittest
from divine_agents import Agent, SharedMemory, AgentNetwork, DeepReflection


class TestAgentNetwork(unittest.TestCase):
    def test_network_evolution(self):
        memory = SharedMemory()
        network = AgentNetwork(memory)
        a1 = Agent("A1", tension=0.8)
        a2 = Agent("A2", tension=0.65)
        network.add_agent(a1)
        network.add_agent(a2)

        network.evolve_agents()

        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")

    def test_deep_reflection(self):
        memory = SharedMemory()
        memory.record_event("past event")
        agent = Agent("A", state="Jaz")
        reflection = DeepReflection(agent, memory)
        new_state = reflection.perform()
        self.assertEqual(new_state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
