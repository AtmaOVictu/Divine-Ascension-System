import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.paradoxical_agent import ParadoxicalAgent


class TestParadoxicalAgent(unittest.TestCase):
    def test_paradox_question(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("jaz res", agent.ask_paradox())

    def test_emotional_response(self):
        agent = ParadoxicalAgent("P", state="Jaz")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("čustva", reply)


if __name__ == "__main__":
    unittest.main()

