import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, problem_dialogue


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

    def test_problem_solving(self):
        agent = Agent("Ana")
        agent.perceive_problem("Razumevanje")
        state = agent.solve_problem()
        self.assertEqual(state, "Jaz")

    def test_dialogue_history(self):
        a1 = Agent("Ana")
        a2 = Agent("Jan", state="Jaz")
        problem_dialogue(a1, a2, "iskanje", "povezovanje")
        self.assertGreater(len(a1.dialogue_history), 0)
        question, _ = a1.dialogue_history[0]
        self.assertIn("Kaj je resnica?", question)


if __name__ == '__main__':
    unittest.main()
