import unittest
from divine_agents import Agent, SuperpositionalAgent, hybrid_dialogue


class TestSuperpositionalAgent(unittest.TestCase):
    def test_collapse_and_transition(self):
        agent = SuperpositionalAgent("S", states=["Ego", "Jaz"])
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_hybrid_dialogue(self):
        a1 = Agent("A1")
        a2 = SuperpositionalAgent("S2", states=["Ego", "Jaz"])
        lines = hybrid_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
