import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_ego_to_jaz(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state="Jaz")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_emotion_clamping(self):
        agent = Agent("C")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)
        self.assertLessEqual(agent.tension, 1.0)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure dialogue references at least one unified truth statement
        self.assertTrue(any("eno" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
