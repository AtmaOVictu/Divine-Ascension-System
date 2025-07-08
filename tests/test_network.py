import unittest
from divine_agents.agent import Agent
from divine_agents.network import AgentNetwork, SharedMemory
from divine_agents.dialogue import philosophical_dialogue


class TestAgentNetwork(unittest.TestCase):
    def test_shared_reflections(self):
        memory = SharedMemory()
        network = AgentNetwork(memory)
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        network.add_agent(a1)
        network.add_agent(a2)
        refs = network.share_reflections()
        self.assertEqual(len(refs), 2)
        self.assertEqual(len(memory.retrieve_history()), 2)

    def test_evolve_agents(self):
        memory = SharedMemory()
        memory.record_event("conflict arises")
        network = AgentNetwork(memory)
        agent = Agent("A")
        network.add_agent(agent)
        network.evolve_agents()
        self.assertEqual(agent.state, "Jaz")

    def test_dialogue_memory(self):
        memory = SharedMemory()
        a1 = Agent("A1", shared_memory=memory)
        a2 = Agent("A2", state="Jaz", shared_memory=memory)
        philosophical_dialogue(a1, a2, memory)
        self.assertTrue(len(memory.retrieve_history()) >= 3)


if __name__ == '__main__':
    unittest.main()
