import unittest
from divine_agents.agent import DynamicAgent
from divine_agents.dialogue import advanced_dialogue
from divine_agents.dynamics import EmotionalTensionDynamics
from divine_agents.evolution import crossover


class TestDynamicAgent(unittest.TestCase):
    def test_multi_layer_transition(self):
        agent = DynamicAgent("D", emotion=0.6, tension=0.8)
        state = agent.multi_layer_transition()
        self.assertEqual(state, "Jaz")

    def test_communication(self):
        a1 = DynamicAgent("A1", emotion_label="angry")
        a2 = DynamicAgent("A2", state="Jaz", emotion_label="happy")
        lines = advanced_dialogue(a1, a2)
        self.assertTrue(any("relativna" in line for line in lines))

    def test_emotion_dynamics(self):
        agent = DynamicAgent("E", emotion_label="angry")
        dyn = EmotionalTensionDynamics(agent)
        dyn.adjust_tension()
        self.assertGreater(agent.tension, 0.0)

    def test_crossover(self):
        child = crossover([1, 2, 3], [4, 5, 6])
        self.assertEqual(len(child), 3)


if __name__ == "__main__":
    unittest.main()
