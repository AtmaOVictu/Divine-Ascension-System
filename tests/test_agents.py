import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        # History should contain the initial and new state
        self.assertEqual(len(agent.history), 2)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_no_duplicate_when_state_unchanged(self):
        agent = Agent("B")
        # First transition causes a state change
        agent.update_tension(0.8)
        agent.transition()
        history_length_after_change = len(agent.history)

        # Reset tension and perform transition without exceeding thresholds
        agent.update_tension(0.1)
        agent.transition()
        # History length should remain the same since state didn't change
        self.assertEqual(len(agent.history), history_length_after_change)


if __name__ == '__main__':
    unittest.main()
