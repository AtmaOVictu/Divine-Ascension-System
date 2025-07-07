import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_with_emotion(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion("fear", 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue agent1 transitions to Jaz and agent2 may reach Enotnost
        self.assertTrue(any(("Jaz" in line or "Enotnost" in line) for line in lines))


if __name__ == '__main__':
    unittest.main()
