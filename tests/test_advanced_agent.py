import os
import sys
import unittest

# Ensure package import works when tests run directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.advanced_agent import AdvancedAgent


class TestAdvancedAgent(unittest.TestCase):
    def test_birth_and_parent_params_affect_state(self):
        birth = {"initial_tension": 0.5, "initial_emotion": 0.2}
        parent = {"parental_tension": 0.3, "parental_emotion": 0.4, "parental_pathos": 0.1}
        agent = AdvancedAgent("Child", birth_params=birth, parent_params=parent)
        # After initialization, optimize_transition should trigger a state change
        agent.optimize_transition()
        self.assertEqual(agent.state, "Jaz")

    def test_emotional_response(self):
        agent = AdvancedAgent("A", emotion=0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Močno", reply)


if __name__ == "__main__":
    unittest.main()
