import os
import sys
import unittest

# Ensure repository root is on the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, KnowledgeBase
from divine_agents.dialogue import philosophical_dialogue


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


class TestKnowledgeBase(unittest.TestCase):
    def test_copy_and_print(self):
        kb = KnowledgeBase()
        tasks = kb.copy_from_library("naloge")
        self.assertEqual(tasks, ["samospoznanje", "logični prehod", "emotivni prehod"])
        out = kb.print_from_library("naloge")
        self.assertIn("naloge", out)


if __name__ == "__main__":
    unittest.main()
