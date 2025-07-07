import unittest
import os
import sys

# Ensure project root is in the Python path so modules can be imported when
# running the tests directly or via pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
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

    def test_emotional_influence(self):
        agent = Agent("B")
        agent.feel("strah", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)


if __name__ == '__main__':
    unittest.main()
