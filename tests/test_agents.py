import unittest
from divine_agents import Agent, Emotion, philosophical_dialogue, ExternalIntegrationLayer


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6, Emotion.JOY)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_external_integration(self):
        agent = Agent("X")
        layer = ExternalIntegrationLayer(agent)
        layer.update_agent_state("new_data")
        self.assertIn(agent.state, ["Jaz", "Enotnost"])



if __name__ == '__main__':
    unittest.main()
