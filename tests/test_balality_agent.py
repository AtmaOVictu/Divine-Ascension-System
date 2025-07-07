import unittest
from divine_agents.balality_agent import BalalityAgent, balality_dialogue


class TestBalalityAgent(unittest.TestCase):
    def test_transition_via_emotion(self):
        agent = BalalityAgent("B")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_reflect_on_duality(self):
        agent = BalalityAgent("B", state="Enotnost")
        reflection = agent.reflect_on_duality()
        self.assertIn("enotnost", reflection.lower())

    def test_balality_dialogue(self):
        a1 = BalalityAgent("B1")
        a2 = BalalityAgent("B2", state="Jaz")
        lines = balality_dialogue(a1, a2)
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
