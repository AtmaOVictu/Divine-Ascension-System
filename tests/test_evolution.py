import unittest
from divine_agents import Agent
from divine_agents.evolution import biological_transition, social_transition


class TestEvolution(unittest.TestCase):
    def test_emotion_trigger_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_biological_transition(self):
        agent = Agent("C")
        state = biological_transition(agent, 0.6)
        self.assertEqual(state, "Jaz")

    def test_social_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        social_transition(a1, a2)
        a1.transition()
        a2.transition()
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
