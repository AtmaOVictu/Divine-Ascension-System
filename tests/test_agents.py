import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    def test_moral_decision(self):
        agent = Agent("A", loyalty=0.8, emotional_state="fearful")
        decision = agent.make_moral_decision("test")
        self.assertIn("help others", decision)

    def test_collaborative_task(self):
        a1 = Agent("A1", loyalty=0.8, emotional_state="happy")
        a2 = Agent("A2", loyalty=0.8, emotional_state="happy")
        result = a1.collaborative_task([a1, a2])
        self.assertIn("successfully", result)


if __name__ == '__main__':
    unittest.main()
