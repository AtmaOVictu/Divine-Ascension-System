import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion_only(self):
        """Agent should transition when emotion alone exceeds threshold."""
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_on_boundary(self):
        """Thresholds are strict; boundary values should not trigger."""
        agent = Agent("C")
        agent.update_tension(0.7)
        state = agent.transition()
        self.assertEqual(state, "Ego")

        agent = Agent("C2")
        agent.update_emotion(0.5)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_history_records_states(self):
        agent = Agent("D")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
