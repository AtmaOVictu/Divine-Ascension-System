import unittest
from divine_agents.agent import Agent
from divine_agents.entertainment import (
    KvizZabavnost,
    UgankaZabavnost,
    IgraOdlocanja,
)


class TestEntertainment(unittest.TestCase):
    def test_quiz_answer(self):
        quiz = KvizZabavnost()
        question = quiz.questions[0]
        self.assertTrue(quiz.check_answer(question, 0))
        self.assertFalse(quiz.check_answer(question, 2))

    def test_uganka_solution(self):
        self.assertTrue(UgankaZabavnost.check_solution("Napetost v prehodu"))
        self.assertFalse(UgankaZabavnost.check_solution("napa\u010den odgovor"))

    def test_game_decision_transition(self):
        agent = Agent("T")
        game = IgraOdlocanja(agent)
        game.decide(True)  # tension should increase
        self.assertGreaterEqual(agent.tension, 0.5)
        # After repeated decisions tension crosses threshold -> state changes
        for _ in range(2):
            game.decide(True)
        self.assertIn(agent.state, ["Jaz", "Enotnost"])


if __name__ == "__main__":
    unittest.main()

