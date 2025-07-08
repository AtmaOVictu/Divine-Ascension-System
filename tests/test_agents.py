import sys
from pathlib import Path
import unittest

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

    def test_numerology_action(self):
        agent = Agent("A", numerology_number=1)
        action = agent.perform_action()
        self.assertEqual(action, "Help")

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.9)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("čustva", response)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("ukrepa" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
