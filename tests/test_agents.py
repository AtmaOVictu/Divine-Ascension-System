import unittest
from divine_agents.agent import Agent, AdvancedAgent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_evolve_and_transition(self):
        agent = Agent("A")
        agent.update_tension(0.6)
        # tension is evolved via logistic/logarithmic functions
        self.assertGreater(agent.tension, 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_advanced_agent(self):
        agent = AdvancedAgent("B", emotion_type="positive")
        agent.update_emotion(0.6)
        # positive emotion should increase tension sufficiently
        self.assertGreater(agent.tension, 0.0)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
