import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.time_module import TimeModule
from divine_agents.history_module import HistoryModule
from divine_agents.space_module import SpaceModule
from divine_agents.language_module import LanguageModule
from divine_agents.agent import Agent


class TestModules(unittest.TestCase):
    def test_time_module(self):
        tm = TimeModule()
        tm.update_time()
        self.assertGreaterEqual(tm.elapsed_time, 0)
        tm.reset_time()
        self.assertLess(tm.elapsed_time, 0.001)

    def test_history_module(self):
        hm = HistoryModule()
        hm.record_event("conflict", "angry", "utilitarian")
        self.assertEqual(len(hm.review_history()), 1)
        hm.record_event("conflict", "angry", "utilitarian")
        hm.record_event("conflict", "angry", "utilitarian")
        hm.record_event("conflict", "angry", "utilitarian")
        self.assertEqual(hm.learn_from_history(), "relativist")

    def test_space_module(self):
        sm = SpaceModule()
        sm.add_agent_to_space("A", (0, 0))
        sm.add_agent_to_space("B", (3, 4))
        self.assertEqual(sm.check_proximity("A", "B"), 5)

    def test_language_module(self):
        a = Agent("A")
        lm = LanguageModule(a)
        lm.process_input("I am angry")
        a.transition()
        self.assertIn(a.state, ["Jaz", "Enotnost"])
        resp = lm.generate_response()
        self.assertTrue(resp)


if __name__ == "__main__":
    unittest.main()
