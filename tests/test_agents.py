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

    def test_history_records_only_transitions(self):
        agent = Agent("H")

        # No threshold exceeded; history should remain unchanged
        agent.transition()
        self.assertEqual(agent.history, ["Ego"])

        # Transition to Jaz when tension exceeds threshold
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

        # Transition call with low tension should not change history
        agent.update_tension(0.2)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

        # Next transition to Enotnost
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()
