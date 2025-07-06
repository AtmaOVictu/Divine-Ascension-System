import os
import sys
import unittest

# Ensure package root is on the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import Agent, AgentState, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, AgentState.JAZ)

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, AgentState.JAZ)

    def test_responses(self):
        agent = Agent("A", state=AgentState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=AgentState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        # At least one line should show the unified truth after transitions
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
