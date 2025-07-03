import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        """Agent should transition when tension exceeds threshold."""
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_driven_transition(self):
        """Emotion intensity triggers state change."""
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        """Responses should reflect philosophical state."""
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        """Dialogue should cause at least one state transition."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure lines mention transitions and philosophical principles
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertTrue(any("absolutna" in line or "relativna" in line or "eno" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
