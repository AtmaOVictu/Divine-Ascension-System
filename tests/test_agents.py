import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.conversation import dynamic_debate


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

    def test_emotion_trigger(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_dynamic_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        transcript = dynamic_debate(a1, a2, rounds=2)
        self.assertTrue(any("prehaja" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
