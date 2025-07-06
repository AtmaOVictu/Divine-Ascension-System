import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.utils import evaluate_equation, generate_major_scale


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_evaluate_equation(self):
        result = evaluate_equation("sin(pi/2)")
        self.assertAlmostEqual(result, 1.0)

    def test_generate_scale(self):
        scale = generate_major_scale("C")
        self.assertEqual(len(scale), 7)
        self.assertEqual(scale[0], "C")


if __name__ == '__main__':
    unittest.main()
