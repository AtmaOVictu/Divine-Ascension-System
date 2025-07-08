import unittest
import time

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.time_module import TimeModule
from divine_agents.history_module import HistoryModule
from divine_agents.space_module import SpaceModule
from divine_agents.language_module import LanguageModule


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


class TestModules(unittest.TestCase):
    def test_history_learning(self):
        history = HistoryModule()
        for _ in range(4):
            history.record_event("conflict", 0.4, "utilitarian")
        self.assertEqual(history.learn_from_history(), "relativist")

    def test_time_module(self):
        tm = TimeModule()
        time.sleep(0.01)
        self.assertGreater(tm.update_time(), 0)

    def test_space_module(self):
        space = SpaceModule()
        space.add_agent("a", (0, 0))
        space.add_agent("b", (3, 4))
        self.assertEqual(space.check_proximity("a", "b"), 5.0)

    def test_language_module(self):
        agent = Agent("A")
        lang = LanguageModule(agent)
        self.assertIn("absolutna", lang.generate_response())
        agent.update_emotion(0.8)
        agent.transition()
        self.assertIn("relativna", lang.generate_response())


if __name__ == '__main__':
    unittest.main()
