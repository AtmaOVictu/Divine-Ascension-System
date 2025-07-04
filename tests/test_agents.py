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

    def test_history_updates_only_on_state_change(self):
        agent = Agent("Hist")
        initial_len = len(agent.history)

        # No transition should occur - tension below threshold
        agent.update_tension(0.2)
        agent.transition()
        self.assertEqual(len(agent.history), initial_len)
        self.assertEqual(agent.state, "Ego")

        # First real transition
        agent.update_tension(1.0)
        agent.transition()
        self.assertEqual(len(agent.history), initial_len + 1)
        self.assertEqual(agent.state, "Jaz")

        # Second real transition
        agent.transition()
        self.assertEqual(len(agent.history), initial_len + 2)
        self.assertEqual(agent.state, "Enotnost")

        # No transition beyond "Enotnost"
        agent.transition()
        self.assertEqual(len(agent.history), initial_len + 2)


if __name__ == '__main__':
    unittest.main()
