import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggers_transition(self):
        """Transition should occur when emotion exceeds threshold even if tension does not."""
        scenarios = [("Ego", "Jaz"), ("Jaz", "Enotnost")]
        for start, expected in scenarios:
            with self.subTest(start=start):
                agent = Agent("A", state=start)
                agent.update_emotion(0.6)  # sets tension to 0.6 (<0.7)
                state = agent.transition()
                self.assertEqual(state, expected)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue_statements(self):
        """Dialogue should include philosophical statements for all states."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        expected = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        for state, phrase in expected.items():
            with self.subTest(state=state):
                self.assertTrue(any(phrase in line for line in lines))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_multiple_transitions(self):
        """History should record each state after multiple transitions."""
        agent = Agent("A")
        agent.update_emotion(0.6)
        agent.transition()
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()
