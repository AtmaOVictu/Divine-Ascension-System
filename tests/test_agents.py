import unittest
import sys
from pathlib import Path

# Ensure package root is on the path for direct test execution
sys.path.append(str(Path(__file__).resolve().parents[1]))

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

    def test_update_emotion_accumulates(self):
        agent = Agent("B")
        agent.update_emotion(0.2, "fear")
        agent.update_emotion(0.3, "joy")
        self.assertAlmostEqual(agent.emotion, 0.5)
        expected_tension = 0.2 * 1.2 + 0.3 * 0.5
        self.assertAlmostEqual(agent.tension, expected_tension)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
