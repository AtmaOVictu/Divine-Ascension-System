import unittest
from divine_agents.agent import Agent, HiddenAgent
from divine_agents.dialogue import philosophical_dialogue, extended_dialogue


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

    def test_hidden_agent_factors(self):
        agent = HiddenAgent("H")
        agent.update_emotion(0.3)
        agent.update_hidden_factors()
        agent.update_emotion(0.6)
        agent.update_hidden_factors()
        self.assertGreater(agent.hidden_factors["hidden_tension"], 0)

    def test_extended_dialogue(self):
        a1 = HiddenAgent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = extended_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
