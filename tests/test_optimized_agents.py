import unittest
from divine_agents.optimized_agent import OptimizedAgent
from divine_agents.dialogue import dynamic_philosophical_dialogue


class TestOptimizedAgent(unittest.TestCase):
    def test_transition_on_emotion(self):
        agent = OptimizedAgent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.state, "Jaz")

    def test_transition_on_tension(self):
        agent = OptimizedAgent("A")
        agent.tension = 0.8
        agent.optimize_transition()
        self.assertEqual(agent.state, "Jaz")

    def test_response_content(self):
        agent = OptimizedAgent("A", state="Jaz")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)

    def test_dynamic_dialogue(self):
        a1 = OptimizedAgent("A1")
        a2 = OptimizedAgent("A2", state="Jaz")
        lines = dynamic_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
