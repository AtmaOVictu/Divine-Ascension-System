import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        """Agent should change state when thresholds are exceeded."""
        by_tension = Agent("A")
        by_tension.update_tension(0.8)
        self.assertEqual(by_tension.transition(), "Jaz")

        by_emotion = Agent("B")
        by_emotion.update_emotion(0.6)
        self.assertEqual(by_emotion.transition(), "Jaz")

    def test_responses(self):
        """Responses should reflect ontological and emotional state."""
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("čustva", reply)

    def test_dialogue(self):
        """Dialogue triggers state transitions and contains unified truth."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
