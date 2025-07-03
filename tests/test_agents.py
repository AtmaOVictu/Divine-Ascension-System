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

    def test_history_records_actual_transitions(self):
        agent = Agent("B")
        # No transition should occur
        agent.transition()
        self.assertEqual(agent.history, ["Ego"])

        # First transition
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

        # Second transition to final state
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])
        self.assertTrue(agent.reached_enotnost)

        # Further transitions should not alter history
        agent.update_tension(1.0)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()
