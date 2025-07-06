import unittest
from divine_agents.agent import Agent
from divine_agents.module import AgentModule
from divine_agents.system import DynamicAgentSystem


class TestModuleInteractions(unittest.TestCase):
    def test_module_dialogue_transitions(self):
        mod1 = AgentModule("Mod1")
        mod2 = AgentModule("Mod2")
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        mod1.add_agent(a1)
        mod2.add_agent(a2)
        lines = mod1.dialogue_with(mod2, "Kaj je resnica?")
        self.assertIn(a1.state, ("Jaz", "Enotnost"))
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("absolutna" in l for l in lines))
        self.assertTrue(any("relativna" in l for l in lines))

    def test_system_run(self):
        mod1 = AgentModule("Mod1")
        mod2 = AgentModule("Mod2")
        mod1.add_agent(Agent("A1"))
        mod2.add_agent(Agent("A2", state="Jaz"))
        system = DynamicAgentSystem()
        system.add_module(mod1)
        system.add_module(mod2)
        lines = system.run("Kaj je resnica?")
        self.assertGreaterEqual(len(lines), 4)


if __name__ == "__main__":
    unittest.main()
