import unittest
from divine_agents.agent import Agent
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

    def test_dialogue_custom_emotions_no_transition(self):
        """Dialogue should not trigger transitions if emotions are low."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.3, emotion2=0.3)
        self.assertFalse(any("prehaja" in line and "Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Ego")
        self.assertEqual(a2.state, "Jaz")

    def test_dialogue_custom_emotions_with_transition(self):
        """Dialogue should respect custom emotion thresholds."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.9, emotion2=0.7)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
