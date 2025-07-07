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

    def test_emotion_transition(self):
        """Agent should transition when emotion threshold exceeded."""
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_history_tracking(self):
        """Verify history records all state changes."""
        agent = Agent("C")
        # First transition triggered by high tension
        agent.update_tension(0.9)
        agent.transition()
        # Second transition triggered by emotion
        agent.update_emotion(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Verify transitions occurred as expected
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        # Dialogue lines should reflect these states
        self.assertIn("A1 prehaja v stanje: Jaz", lines[2])
        self.assertIn("A2 prehaja v stanje: Enotnost", lines[3])
        # Ensure final lines include responses from current states
        self.assertIn(a1.respond("Kaj je resnica?"), lines[4])
        self.assertIn(a2.respond("Kaj je resnica?"), lines[5])


if __name__ == '__main__':
    unittest.main()
