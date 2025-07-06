import unittest

from divine_agents.agent import Agent
from divine_agents.automation import (
    AutomatskiPrehodi,
    SamodejnaOptimizacija,
    QLearningAgent,
    SamodejnoUcenje,
)


class TestAutomation(unittest.TestCase):
    def test_auto_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        auto = AutomatskiPrehodi(agent)
        state = auto.preveri_pogoje_za_prehod()
        self.assertEqual(state, "Jaz")

    def test_optimizacija(self):
        agent = Agent("A", tension=0.9)
        agent.history.append("error")
        opti = SamodejnaOptimizacija(agent)
        opti.optimiziraj_kodo()
        self.assertLess(agent.tension, 0.9)

    def test_q_learning_update(self):
        actions = ["a", "b"]
        agent = QLearningAgent("Q", actions)
        learner = SamodejnoUcenje(agent)
        learner.learn_from_experience("s1", "a", 1.0, "s2")
        self.assertIn("a", agent.q_table.get("s1", {}))


if __name__ == "__main__":
    unittest.main()

