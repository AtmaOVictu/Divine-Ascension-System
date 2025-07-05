import unittest
from divine_agents import (
    EmotionSystem,
    EthicalAssessment,
    KrepitvenoUcenje,
    MultidimensionalAgent,
    TransitionVisualizer,
    RealDataConnection,
)


class TestAdvancedComponents(unittest.TestCase):
    def test_emotion_change(self):
        e = EmotionSystem()
        e.change_emotion("Veselje")
        self.assertEqual(e.emotion, "Veselje")

    def test_ethics(self):
        judge = EthicalAssessment()
        self.assertEqual(judge.assess("egoizem"), "Neetično")
        self.assertEqual(judge.assess("altruizem"), "Etično")

    def test_learning(self):
        learner = KrepitvenoUcenje()
        self.assertEqual(learner.izberi_akcijo(), "Aktiviraj")
        self.assertEqual(learner.state, "Aktivacija")

    def test_multidimensional(self):
        agent = MultidimensionalAgent("M")
        results = agent.act_across_dimensions()
        self.assertEqual(len(results), 3)

    def test_visualizer_and_real_data(self):
        vis = TransitionVisualizer()
        vis.add_transition("Ego", 0.2)
        self.assertEqual(len(vis.transitions), 1)
        data = RealDataConnection(stres=8, razpolozenje=2)
        msg = data.read_data()
        self.assertIn("stres", msg.lower())


if __name__ == "__main__":
    unittest.main()
