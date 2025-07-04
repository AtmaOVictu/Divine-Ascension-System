import unittest
from divine_agents.agent import Agent, DynamicAgent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.integration import ExternalIntegrationLayer


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

    def test_dynamic_agent_adapts(self):
        agent = DynamicAgent("Dyn", adaptability=True)
        agent.update_tension(0.9)
        agent.transition()
        self.assertLess(agent.tension, 0.9)

    def test_external_integration(self):
        agent = Agent("Ext")
        layer = ExternalIntegrationLayer(agent)
        layer.update_agent_state("new_data")
        self.assertEqual(agent.state, "Jaz")
        layer.update_agent_state("new_data")
        self.assertEqual(agent.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
