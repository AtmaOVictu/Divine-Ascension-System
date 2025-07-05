import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.paradoxical_agent import ParadoxicalAgent


class TestParadoxicalAgent(unittest.TestCase):
    def test_paradox_question_changes_with_state(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("Ali sem jaz res", agent.ask_paradox())
        agent.update_tension(0.8)
        agent.transition()
        self.assertIn("Ali sem to", agent.ask_paradox())

    def test_paradox_response_contains_base_philosophy(self):
        agent = ParadoxicalAgent("P", state="Enotnost")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("medsebojno", response)
        self.assertIn("Kako lahko vse resnice", response)


if __name__ == '__main__':
    unittest.main()
