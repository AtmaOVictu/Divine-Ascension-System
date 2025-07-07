import unittest
from divine_agents import Agent, philosophical_dialogue, Affirmation, Negation


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

    def test_affirmation(self):
        agent = Agent("Aff")
        message = agent.affirm()
        self.assertIn("Affirmation", message)
        self.assertIn(message, agent.history)

    def test_negation(self):
        agent = Agent("Neg", state="Jaz")
        new_state = agent.negate()
        self.assertEqual(new_state, "Ego")


if __name__ == '__main__':
    unittest.main()
