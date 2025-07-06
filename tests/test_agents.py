import unittest
from pathlib import Path
import sys

# Ensure repository root is on the Python path so imports work when tests
# are executed from different locations.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=2)
        # After two rounds the second agent should reach Enotnost
        self.assertIn("Enotnost", a2.state)
        self.assertTrue(any("prehaja" in line for line in lines))

    def test_emotional_response(self):
        agent = Agent("A")
        base_reply = agent.respond("Kaj je resnica?")
        agent.update_emotion(0.9)
        intense_reply = agent.respond("Kaj je resnica?")
        self.assertNotEqual(base_reply, intense_reply)
        self.assertIn("čutim", intense_reply.lower())


if __name__ == '__main__':
    unittest.main()
