import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

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

        agent.update_emotion(0.6, "joy")
        joyful_reply = agent.respond("Kaj je resnica?")
        self.assertIn("veseljem", joyful_reply.lower())

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure at least one transition occurred
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        # After dialogue, agent1 should not be in Ego state anymore
        self.assertNotEqual(a1.state, "Ego")


if __name__ == '__main__':
    unittest.main()
