import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.apply_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.apply_emotion("joy", 0.9)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("(veselo)"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue agent2 should reach Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Emotional prefix should be present in responses
        self.assertTrue(
            any("(" in line.split(":", 1)[1].strip() for line in lines if "A1:" in line or "A2:" in line)
        )


if __name__ == '__main__':
    unittest.main()
