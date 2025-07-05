import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.oracle import OracleAgent


class TestOracleAgent(unittest.TestCase):
    def test_records_transition(self):
        agent = OracleAgent("O")
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(len(agent.transitions), 1)
        self.assertEqual(agent.transitions[0]["from"], "Ego")
        self.assertEqual(agent.transitions[0]["to"], "Jaz")

    def test_suggest_and_predict(self):
        agent = OracleAgent("O")
        agent.update_tension(0.9)
        agent.transition()
        agent.update_tension(0.9)
        agent.transition()
        self.assertIn("Jaz", agent.suggest_next_step("Ego"))
        self.assertEqual(agent.predict_future(), "Enotnost")


if __name__ == "__main__":
    unittest.main()
