import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # Without key the agent should not transition
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Ego")

        # Grant key and transition should occur
        agent.acquire_key("Ego_to_Jaz")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # Lock should block further transition
        agent.acquire_key("Jaz_to_Enotnost")
        agent.add_lock("no_move")
        agent.update_tension(1.0)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.9)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("Čutim močna čustva", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # After dialogue agent1 should have moved to Jaz
        self.assertEqual(a1.state, "Jaz")
        # Ensure emotional note is present in at least one response
        self.assertTrue(any("Čutim močna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
