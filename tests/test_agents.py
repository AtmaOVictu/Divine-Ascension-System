import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        """Agent should transition when emotion threshold is exceeded."""
        agent = Agent("B")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_prefix_change(self):
        """Verify that prefixes reflect state changes during dialogue."""
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("A1 (Ego)", lines[0])
        self.assertIn("A2 (Jaz)", lines[1])
        self.assertIn("A1 prehaja v stanje: Jaz", lines[2])
        self.assertIn("A2 prehaja v stanje: Enotnost", lines[3])


if __name__ == '__main__':
    unittest.main()
