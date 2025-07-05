import unittest
from divine_agents.agent import Agent, EmotionDimensionAgent
from divine_agents.dialogue import philosophical_dialogue, dimension_dialogue


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

    def test_dimension_dialogue(self):
        a1 = EmotionDimensionAgent("D1", dimension=2)
        a2 = EmotionDimensionAgent("D2", dimension=3, state="Jaz")
        lines = dimension_dialogue(a1, a2)
        self.assertTrue(any("vpliv v dimenziji" in line for line in lines))

    def test_dimension_processing(self):
        a1 = EmotionDimensionAgent("A1", dimension=2)
        a1.update_emotion(0.8)
        influence = a1.process_emotion()
        self.assertAlmostEqual(influence, 1.6)


if __name__ == '__main__':
    unittest.main()
