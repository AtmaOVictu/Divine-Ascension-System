import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import Agent, MetaModule, philosophical_dialogue


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

    def test_agent_id_unique(self):
        module = MetaModule()
        a1 = Agent("A1")
        a2 = Agent("A2")
        module.add_agent(a1)
        module.add_agent(a2)
        self.assertNotEqual(a1.agent_id, a2.agent_id)

    def test_execute_equation(self):
        agent = Agent("Math", equation="x**2")
        module = MetaModule()
        module.add_agent(agent)
        result = module.execute_agent_equation(agent, 3)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
