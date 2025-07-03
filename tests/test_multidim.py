import unittest
from divine_agents.multi_dim_agent import MultiDimensionalMoralAgent


class TestMultiDimensionalMoralAgent(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = MultiDimensionalMoralAgent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_tension(self):
        agent = MultiDimensionalMoralAgent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue_line(self):
        a1 = MultiDimensionalMoralAgent("A")
        a2 = MultiDimensionalMoralAgent("B", state="Jaz")
        line = a1.dialogue_line([a2])
        self.assertIn("Resnica je absolutna", line)
        # after increasing emotion, a1 should transition
        a1.update_emotion(0.6)
        a1.transition()
        line2 = a1.dialogue_line([a2])
        self.assertIn("Resnica je relativna", line2)


if __name__ == "__main__":
    unittest.main()
