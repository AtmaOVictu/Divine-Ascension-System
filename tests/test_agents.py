import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.transitions import biological_transition, social_transition


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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_evolve(self):
        agent = Agent("A")
        new_state = agent.evolve(1.0)
        self.assertEqual(new_state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("B")
        agent.update_emotion(0.9)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("custva", response)

    def test_logistic_bounds(self):
        self.assertTrue(0 < biological_transition(0.5) < 1)
        self.assertTrue(0 < social_transition(0.5) < 1)


if __name__ == '__main__':
    unittest.main()
