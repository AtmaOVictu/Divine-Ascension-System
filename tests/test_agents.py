import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_from_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_from_emotion(self):
        agent = Agent("B")
        agent.update_emotion("fear", 0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        jaz = Agent("J", state="Jaz")
        eno = Agent("N", state="Enotnost")
        self.assertIn("absolutna", ego.respond("?"))
        self.assertIn("relativna", jaz.respond("?"))
        self.assertIn("eno", eno.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in l or "Enotnost" in l for l in lines))



if __name__ == '__main__':
    unittest.main()
