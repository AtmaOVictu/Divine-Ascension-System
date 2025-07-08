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

    def test_high_emotion_triggers_transition(self):
        """High emotion should cause a transition even with low tension."""
        agent = Agent("A")
        agent.update_emotion(0.8)
        agent.update_tension(0.2)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_no_transition_below_thresholds(self):
        """Agent should not transition when both emotion and tension are low."""
        agent = Agent("A")
        agent.update_emotion(0.4)
        agent.update_tension(0.3)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertEqual(agent.history, ["Ego", "Ego"])


if __name__ == '__main__':
    unittest.main()
