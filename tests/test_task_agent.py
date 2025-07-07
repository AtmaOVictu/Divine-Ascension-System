import unittest
from divine_agents.task_agent import TaskAgent, Krak


class TestTaskAgent(unittest.TestCase):
    def test_krak_activation_on_emotion(self):
        agent = TaskAgent("A1")
        krak = Krak("emotion", "high_emotion")
        agent.add_krak(krak)
        agent.update_emotion(0.8)
        agent.transition()
        self.assertTrue(krak.completed)

    def test_krak_activation_on_state(self):
        agent = TaskAgent("A1")
        krak = Krak("to_jaz", "state_jaz")
        agent.add_krak(krak)
        agent.update_tension(0.8)
        agent.transition()
        self.assertTrue(krak.completed)


if __name__ == "__main__":
    unittest.main()

