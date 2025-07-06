import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, AgentWithHistory
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("anger", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = AgentWithHistory("A1")
        a2 = AgentWithHistory("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


class TestComplexTransitions(unittest.TestCase):
    def test_history_based_transition(self):
        agent = AgentWithHistory("Hist")
        for _ in range(4):
            agent.update_emotion("anger", 0.8)
            agent.transition()
        self.assertIn(agent.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
