import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.config import DEEP_THOUGHT_CONFIG


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.5)
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

    def test_deep_thought_config(self):
        self.assertEqual(DEEP_THOUGHT_CONFIG["ontological_key"], "deep_thought_mode")


if __name__ == '__main__':
    unittest.main()
