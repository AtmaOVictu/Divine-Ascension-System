import unittest

from divine_agents.agent import Agent
from divine_agents.krak import Krak


class TestKrakActivation(unittest.TestCase):
    def test_activation_by_emotion(self):
        agent = Agent("A")
        krak = Krak("High Emotion", lambda a: a.emotion > 0.7)
        agent.add_krak(krak)
        agent.update_emotion(0.8)
        self.assertTrue(krak.completed)

    def test_activation_by_state_transition(self):
        agent = Agent("A")
        krak = Krak("To Jaz", lambda a: a.state == "Jaz")
        agent.add_krak(krak)
        agent.update_tension(0.8)
        agent.transition()
        self.assertTrue(krak.completed)


if __name__ == "__main__":
    unittest.main()
