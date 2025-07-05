import unittest
from divine_agents.optimized_agent import OptimizedAgent
from divine_agents.dialogue import optimized_philosophical_dialogue


class TestOptimizedAgent(unittest.TestCase):
    def test_transition_with_high_emotion(self):
        agent = OptimizedAgent("O1")
        agent.update_emotion(0.9)
        self.assertEqual(agent.state, "Jaz")

    def test_emotional_feedback(self):
        agent = OptimizedAgent("O2", emotion=0.8)
        feedback = agent.respond("Kaj je resnica?")
        self.assertIn("Močno čustvujem", feedback)

    def test_optimized_dialogue(self):
        a1 = OptimizedAgent("A1")
        a2 = OptimizedAgent("A2", state="Jaz")
        lines = optimized_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
