import unittest
from divine_agents.learning_agent import LearningAgent
from divine_agents.dialogue import learning_dialogue


class TestLearningAgent(unittest.TestCase):
    def test_learning_transition(self):
        agent = LearningAgent("L")
        agent.feel(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_clustering(self):
        agent = LearningAgent("L")
        for _ in range(3):
            agent.feel(0.9)
            agent.transition()
        self.assertIsInstance(agent.cluster, int)

    def test_learning_dialogue(self):
        a1 = LearningAgent("A1")
        a2 = LearningAgent("A2", state="Jaz")
        lines = learning_dialogue(a1, a2)
        self.assertTrue(any("cluster" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
