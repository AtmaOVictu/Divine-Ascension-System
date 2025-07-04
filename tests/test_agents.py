import unittest
import sys
from pathlib import Path

# Ensure package is discoverable when tests run via pytest
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
        lines = philosophical_dialogue(a1, a2)
        # after the dialogue agents should at least mention Enotnost or show synonym link
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn("Sinonimna naveza", " ".join(a1.history))

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.9)
        # High emotion should modify tone (uppercase)
        response = agent.respond("Kaj je resnica?")
        self.assertEqual(response, response.upper())


if __name__ == '__main__':
    unittest.main()
