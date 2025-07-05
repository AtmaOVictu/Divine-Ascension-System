import os
import sys
import unittest

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

    def test_value_clamping(self):
        agent = Agent("C", tension=1.5, emotion=-0.2)
        self.assertEqual(agent.tension, 1.0)
        self.assertEqual(agent.emotion, 0.0)
        agent.update_emotion(1.3)
        self.assertLessEqual(agent.emotion, 1.0)
        agent.update_tension(-0.5)
        self.assertGreaterEqual(agent.tension, 0.0)

    def test_contact_version(self):
        a1 = Agent("A1", state="Ego")
        a2 = Agent("A2", state="Jaz")
        a1.contact(a2)
        self.assertEqual(a1.version, "verzija 2")


if __name__ == '__main__':
    unittest.main()
