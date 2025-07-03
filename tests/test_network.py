import unittest
from divine_agents.agent import Agent
from divine_agents.network import Module, AgentNetwork


class TestNetwork(unittest.TestCase):
    def test_module_run_triggers_transition(self):
        agent = Agent("A")
        module = Module("M")
        module.add_agent(agent)
        lines = module.run()
        self.assertIn("A", lines[0])
        self.assertEqual(agent.state, "Jaz")

    def test_bridge_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        m1 = Module("M1"); m1.add_agent(a1)
        m2 = Module("M2"); m2.add_agent(a2)
        network = AgentNetwork(); network.add_module(m1); network.add_module(m2)
        lines = network.bridge_dialogue()
        self.assertTrue(any("Resnica" in l for l in lines))
        self.assertIn("Enotnost", " ".join(lines))


if __name__ == '__main__':
    unittest.main()
