import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    """Unit tests for ontological agent behaviour."""

    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_multiple_transitions(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.6)
        final_state = agent.transition()
        self.assertEqual(final_state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        combined = "\n".join(lines)
        self.assertIn("absolutna", combined)
        self.assertIn("relativna", combined)


if __name__ == '__main__':
    unittest.main()
