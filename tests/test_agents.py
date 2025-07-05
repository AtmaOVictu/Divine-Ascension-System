import unittest
from divine_agents.agent import Agent, AdvancedCodexAgent
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

    def test_advanced_evolve_and_transition(self):
        adv = AdvancedCodexAgent("Adv", emotion_type="positive")
        adv.update_emotion(0.6)
        adv.evolve()
        state = adv.transition()
        self.assertIn(state, ("Jaz", "Enotnost"))


if __name__ == '__main__':
    unittest.main()
