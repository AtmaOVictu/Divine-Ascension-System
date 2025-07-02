import unittest
import sys
from pathlib import Path

# Ensure the package root is on the path for imports
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_when_below_thresholds(self):
        agent = Agent("C")
        agent.update_tension(0.5)
        agent.update_emotion(0.2)  # total tension 0.7, emotion 0.2
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response_prefix(self):
        agent = Agent("D")
        agent.update_emotion(0.8)
        agent.transition()
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Čustveno"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
