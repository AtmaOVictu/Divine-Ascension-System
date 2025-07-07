import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotions import EmotionType


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(EmotionType.JOY, 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("radostjo", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # At least one agent should reach Enotnost during the dialogue
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
