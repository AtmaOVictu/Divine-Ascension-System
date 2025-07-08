import unittest
from divine_agents.agent import Agent
from divine_agents.learning import decay_tension, reinforce, learning_cycle


class TestLearningSystem(unittest.TestCase):
    def test_decay_reduces_tension(self):
        agent = Agent("A", tension=1.0, emotion=0.5)
        decay_tension(agent, time_step=1.0)
        self.assertLess(agent.tension, 1.0)

    def test_reinforce_adjusts_state(self):
        agent = Agent("A", tension=0.5, emotion=0.4)
        reinforce(agent, reward=1.0)
        self.assertLess(agent.tension, 0.5)
        self.assertGreaterEqual(agent.emotion, 0.4)

    def test_learning_cycle_transitions(self):
        a1 = Agent("A1", tension=0.9)
        a2 = Agent("A2", emotion=0.6)
        log = learning_cycle(a1, a2, steps=1)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("resnica" in line.lower() for line in log))


if __name__ == "__main__":
    unittest.main()
