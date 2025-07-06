import unittest
from divine_agents.agent import Agent
from divine_agents.automation import (
    AutomatskiPrehodi,
    SamodejnaOptimizacija,
    QLearningAgent,
    SamodejnoUcenje,
    KolektivniModel,
)


class TestAutomation(unittest.TestCase):
    def test_automatski_prehodi(self):
        agent = Agent("Auto", tension=0.8)
        auto = AutomatskiPrehodi(agent)
        state = auto.preveri_pogoje_za_prehod()
        self.assertEqual(state, "Jaz")

    def test_samodejna_optimizacija(self):
        agent = Agent("Opt", tension=0.5)
        agent.history.append("error")
        opt = SamodejnaOptimizacija(agent)
        opt.optimiziraj_kodo()
        self.assertLess(agent.tension, 0.5)

    def test_q_learning_update(self):
        learner = QLearningAgent(actions=["a", "b"], epsilon=0)
        wrapper = SamodejnoUcenje(Agent("L"), learner)
        wrapper.learn_from_experience("s", "a", 1.0, "s2")
        self.assertIn("a", learner.q_table["s"])

    def test_kolektivni_model(self):
        learner1 = QLearningAgent(actions=["x"], epsilon=0.5)
        learner2 = QLearningAgent(actions=["y"], epsilon=0.5)
        m = KolektivniModel([
            SamodejnoUcenje(Agent("A1"), learner1),
            SamodejnoUcenje(Agent("A2"), learner2),
        ])
        m.kolektivno_ucenje()
        self.assertLessEqual(learner1.epsilon, 0.5)
        self.assertLessEqual(learner2.epsilon, 0.5)


if __name__ == "__main__":
    unittest.main()
