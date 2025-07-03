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
        agent = Agent("A")
        initial_len = len(agent.history)
        # No transition because thresholds not met
        agent.transition()
        self.assertEqual(len(agent.history), initial_len)

        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        self.assertEqual(len(agent.history), initial_len + 1)

        # Calling transition again without change should not extend history
        agent.update_tension(0.0)
        agent.transition()
        self.assertEqual(len(agent.history), initial_len + 1)


if __name__ == '__main__':
    unittest.main()
