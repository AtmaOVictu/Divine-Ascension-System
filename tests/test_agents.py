import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.math_model import transition_score, error_value


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

    def test_complex_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        score = transition_score(agent.tension, agent.emotion, 0.3, 0.4)
        state, err = agent.complex_transition(0.3, 0.4, alpha=1.0)
        expected_err = error_value(score, 1.0)
        self.assertAlmostEqual(err, expected_err)
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
