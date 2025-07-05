import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.fun import KvizZabavnost, UgankaZabavnost, IgraOdlocanja


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

    def test_quiz_answer(self):
        quiz = KvizZabavnost()
        q = quiz.questions[0]
        self.assertTrue(quiz.check_answer(q, 0))

    def test_puzzle_solution(self):
        puzzle = UgankaZabavnost()
        self.assertTrue(puzzle.check_solution("Napetost v prehodu"))

    def test_decision_game_transition(self):
        agent = Agent("B")
        game = IgraOdlocanja(agent)
        new_state = game.make_decision(True)
        self.assertEqual(new_state, "Jaz")


if __name__ == '__main__':
    unittest.main()
