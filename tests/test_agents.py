import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.symbolic import Symbol, Expression


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

    def test_no_transition_without_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.2)
        agent.update_emotion(0.3)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("math" in line for line in lines))

    def test_discuss_expression(self):
        agent = Agent("C", state="Jaz")
        var = Symbol('Š')
        expr = Expression(var)
        result = agent.discuss_expression(expr, var)
        self.assertIn('∫', result)


if __name__ == '__main__':
    unittest.main()
