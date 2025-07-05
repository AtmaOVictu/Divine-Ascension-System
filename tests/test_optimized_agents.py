import unittest
from divine_agents.optimized_agent import OptimizedAgent
from divine_agents.enhanced_dialogue import dynamic_philosophical_dialogue


class TestOptimizedAgent(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = OptimizedAgent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.state, "Jaz")

    def test_transition_by_tension(self):
        agent = OptimizedAgent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_emotional_response(self):
        agent = OptimizedAgent("A", state="Ego")
        agent.update_emotion(0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Močno čustvujem", reply)

    def test_dynamic_dialogue(self):
        a1 = OptimizedAgent("A1")
        a2 = OptimizedAgent("A2", state="Jaz")
        lines = dynamic_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
