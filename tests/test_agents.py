import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.dialogue import philosophical_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("A")
        agent.update_tension(0.3)
        agent.update_emotion(0.4)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_multi_round(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=2, step=0.4)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
