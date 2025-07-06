import unittest
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


class TestProblemSolving(unittest.TestCase):
    def test_problem_recognition_and_solution(self):
        agent = Agent("B")
        agent.recognize_problem("Razumevanje")
        state_before = agent.state
        new_state = agent.solve_problem()
        self.assertNotEqual(state_before, new_state)
        self.assertIn("Recognized problem", agent.events[0])

    def test_problem_dialogue(self):
        a1 = Agent("C1")
        a2 = Agent("C2")
        lines = problem_dialogue(a1, a2, "Iskanje", "Povezava")
        self.assertTrue(any("rešuje problem" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
