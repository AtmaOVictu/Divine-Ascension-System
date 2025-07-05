import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.transformer import EmotionTransformer


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


class TestEmotionTransformer(unittest.TestCase):
    def test_negative_to_positive(self):
        transformer = EmotionTransformer(-0.5)
        val = transformer.transform_positive()
        self.assertGreaterEqual(val, 0)

    def test_positive_to_negative(self):
        transformer = EmotionTransformer(0.6)
        val = transformer.transform_negative()
        self.assertLessEqual(val, 0)


if __name__ == '__main__':
    unittest.main()
