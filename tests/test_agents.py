import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, segmented_dialogue


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

    def test_state_transitions(self):
        agent1 = Agent("A1")
        agent2 = Agent("A2")
        dialogue = segmented_dialogue(agent1, agent2, cycles=5)
        self.assertTrue(any("Jaz" in line for line in dialogue))
        self.assertTrue(any("Enotnost" in line for line in dialogue))

    def test_transition_order(self):
        agent = Agent("Solo")
        segmented_dialogue(agent, agent, cycles=3)
        self.assertIn("Ego", agent.history)
        self.assertIn("Jaz", agent.history)
        self.assertIn("Enotnost", agent.history)

    def test_emotion_triggers_transition(self):
        agent = Agent("Emotion")
        agent.update_emotion(0.8)
        self.assertEqual(agent.transition(), "Jaz")


if __name__ == '__main__':
    unittest.main()
