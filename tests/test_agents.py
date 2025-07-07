import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents import Agent, philosophical_dialogue, debate, TaskManager


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

    def test_debate_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = debate(a1, a2, inc1=0.8, inc2=0.2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")
        self.assertTrue(any("Jaz" in line for line in lines))

    def test_task_manager(self):
        tm = TaskManager()
        b1 = tm.add_open_branch("Krak A")
        b2 = tm.add_open_branch("Krak A")
        tm.close_branch(b1)
        tm.close_branch(b2)
        self.assertEqual(len(tm.history), 0)
        related = tm.find_related_branches(b1)
        self.assertIn(b2, related)


if __name__ == '__main__':
    unittest.main()
