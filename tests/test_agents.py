import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate


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

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.set_emotion("strah", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        a1.set_emotion("jeza", 0.4)
        a2.set_emotion("veselje", 0.4)
        lines = dynamic_debate(a1, a2, rounds=2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
