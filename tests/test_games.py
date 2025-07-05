import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.agent import Agent
from divine_agents.games import KvizZabavnost, UgankaZabavnost, IgraOdlocanja


class TestGames(unittest.TestCase):
    def test_kviz_transition(self):
        agent = Agent("K")
        quiz = KvizZabavnost()
        correct = quiz.ask(0, 0, agent)
        self.assertTrue(correct)
        self.assertEqual(agent.state, "Jaz")

    def test_uganka_no_transition_on_wrong(self):
        agent = Agent("U", state="Jaz")
        puzzle = UgankaZabavnost()
        correct = puzzle.solve("Ne vem", agent)
        self.assertFalse(correct)
        self.assertEqual(agent.state, "Jaz")

    def test_igra_decision_transition(self):
        agent = Agent("D")
        game = IgraOdlocanja(agent)
        state = game.make_decision(True)
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
