import unittest
from divine_agents.agent import Agent, InteractionAgent, FreeWillAgent
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

    def test_external_factor_history(self):
        agent = Agent("A")
        agent.update_external_factors("weather", 0.5)
        self.assertIn("weather", agent.external_factors)
        self.assertTrue(any("weather" in h for h in agent.history))

    def test_interaction(self):
        a1 = InteractionAgent("A1")
        a2 = InteractionAgent("A2")
        a1.interact(a2)
        self.assertIn(a1.interaction_history[-1], {"cooperate", "compete"})

    def test_free_will(self):
        agent = FreeWillAgent("A")
        decision = agent.make_decision()
        self.assertIn(decision, {"bold", "cautious"})
        self.assertTrue(any("Decision" in h for h in agent.history))


if __name__ == '__main__':
    unittest.main()
