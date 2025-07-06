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

    def test_no_transition_low_tension_emotion(self):
        """Agent with low tension and emotion should not change state."""
        agent = Agent("A")
        initial_state = agent.state
        agent.update_tension(0.3)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, initial_state)
        self.assertEqual(agent.history, [initial_state, initial_state])


if __name__ == '__main__':
    unittest.main()
