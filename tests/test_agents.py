import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_no_transition_when_below_threshold(self):
        agent = Agent("A")
        agent.update_tension(0.6)
        self.assertEqual(agent.transition(), "Ego")

    def test_philosophical_responses(self):
        agent = Agent("A")
        self.assertIn("absolutna", agent.respond("Kaj je resnica?"))
        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("Kaj je resnica?"))
        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("Kaj je resnica?"))

    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # At least one transition to Enotnost should happen during the dialogue
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
