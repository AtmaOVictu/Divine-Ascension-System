import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_cycle_with_o(self):
        agent = Agent("A", state="O")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Ego")
        agent.update_emotion(0.9)
        self.assertEqual(agent.transition(), "Jaz")
        agent.update_emotion(0.9)
        self.assertEqual(agent.transition(), "Enotnost")
        agent.update_emotion(0.9)
        self.assertEqual(agent.transition(), "O")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.state = "O"
        reply_o = agent.respond("Kaj je resnica?")
        self.assertIn("Potencial", reply_o)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Potencial" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
