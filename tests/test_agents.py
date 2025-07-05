import unittest
from divine_agents.agent import Agent, ReflectiveAgent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.system import MultiAgentSystem


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_reflective_agent(self):
        agent = ReflectiveAgent("R", state="Enotnost", emotion=0.8)
        agent.history = ["Jaz", "Enotnost"]
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_multi_agent_system(self):
        system = MultiAgentSystem()
        system.add_agent(Agent("A"))
        system.add_agent(Agent("B"))
        system.update_all_agents()
        self.assertEqual(len(system.agents), 2)


if __name__ == '__main__':
    unittest.main()
