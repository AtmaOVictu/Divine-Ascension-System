import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_thresholds(self):
        """Agent should not change state when tension and emotion are low."""
        agent = Agent("A")
        agent.update_tension(0.5)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_transition_jaz_to_enotnost(self):
        """Agent in Jaz should move to Enotnost when thresholds exceeded."""
        agent = Agent("A", state="Jaz")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

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
