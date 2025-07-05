import unittest
from divine_agents.agent import Agent
from divine_agents.fun import UgankaZabavnost, IgraOdlocanja


class TestFunModules(unittest.TestCase):
    def test_puzzle_solution(self):
        puzzle = UgankaZabavnost()
        self.assertTrue(puzzle.solve("Napetost v prehodu"))
        self.assertFalse(puzzle.solve("wrong"))

    def test_decision_game_transition(self):
        agent = Agent("A", tension=0.6)
        game = IgraOdlocanja(agent)
        game.decision(True)
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()
