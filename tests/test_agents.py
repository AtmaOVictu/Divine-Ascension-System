import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_emotion(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("E")
        jaz = Agent("J", state="Jaz")
        eno = Agent("N", state="Enotnost")
        self.assertIn("absolutna", ego.respond("?"))
        self.assertIn("relativna", jaz.respond("?"))
        self.assertIn("eno", eno.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
