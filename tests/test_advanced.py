import unittest
from divine_agents.advanced import MultiLayerAgent


class TestMultiLayerAgent(unittest.TestCase):
    def test_multi_layer_transition_selfish_experience(self):
        agent = MultiLayerAgent("A", tension=0.6, emotional_state="calm")
        agent.add_experience("selfish")
        state = agent.multi_layer_transition()
        self.assertEqual(state, "Enotnost")

    def test_adjust_tension_based_on_emotions(self):
        agent = MultiLayerAgent("A", emotional_state="angry")
        agent.adjust_tension_based_on_emotions()
        self.assertGreaterEqual(agent.tension, 0.3)

    def test_learning_from_past_decisions(self):
        agent = MultiLayerAgent("A")
        agent.add_experience("helped")
        decision = agent.learn_from_past_decisions("danger")
        self.assertEqual(decision, "Act selflessly")


if __name__ == "__main__":
    unittest.main()
