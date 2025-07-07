import unittest
from divine_agents.agent import Agent
from divine_agents.emotional_agent import EmotionalAgent
from divine_agents.dialogue import philosophical_dialogue, emotional_philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = EmotionalAgent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = EmotionalAgent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_color_mapping(self):
        agent = EmotionalAgent("A")
        agent.update_emotion(0.3, "calm")
        self.assertEqual(agent.thought_line, "clear, rational")
        self.assertEqual(agent.COLOR_MAP["calm"], "blue")

    def test_dialogue(self):
        a1 = EmotionalAgent("A1")
        a2 = EmotionalAgent("A2", state="Jaz")
        lines = emotional_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Debate" in line for line in lines))
        self.assertTrue(any("red" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
