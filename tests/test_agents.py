import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, advanced_dialogue
from divine_agents.advanced_agent import AdvancedAgent, logistic_function


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


class TestAdvancedAgent(unittest.TestCase):
    def test_evolve_transition(self):
        agent = AdvancedAgent("Adv")
        agent.update_emotion(0.8)
        new_state = agent.evolve()
        self.assertEqual(new_state, "Jaz")

    def test_logistic_function(self):
        self.assertGreater(logistic_function(1.0, 1.0, 0.0), 0.5)

    def test_advanced_dialogue(self):
        a1 = AdvancedAgent("A1")
        a2 = AdvancedAgent("A2", state="Jaz")
        lines = advanced_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
