import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, multi_round_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("joy")  # intensity 0.7 > 0.5
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion="anger")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("With anger", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = multi_round_dialogue(a1, a2, 2)
        # expect responses and transition logs for each round
        self.assertEqual(len(lines), 8)


if __name__ == '__main__':
    unittest.main()


