import unittest
from divine_agents.agent import Agent
from divine_agents.network import Module, AgentNetwork


class TestModule(unittest.TestCase):
    def test_execute_triggers_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        module = Module("M", "samospoznanje")
        module.add_agent(agent)
        lines = module.execute()
        self.assertEqual(agent.state, "Jaz")
        self.assertTrue(any("Resnica" in line for line in lines))


class TestAgentNetwork(unittest.TestCase):
    def test_simulate_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        m1 = Module("M1", "faza1")
        m2 = Module("M2", "faza2")
        m1.add_agent(a1)
        m2.add_agent(a2)
        network = AgentNetwork()
        network.add_module(m1)
        network.add_module(m2)
        dialogue = network.simulate()
        self.assertTrue(any(state in line for state in ("Jaz", "Enotnost") for line in dialogue))


if __name__ == "__main__":
    unittest.main()
