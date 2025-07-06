import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

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
        self.assertTrue(any("Enotnost" in line for line in lines))
        # verify replication lines are present
        self.assertTrue(any(line.startswith("Kopija:") for line in lines))

    def test_replicate_and_break(self):
        agent = Agent("A")
        agent.update_emotion(0.9)
        agent.transition()
        copy = agent.replicate_truth()
        self.assertTrue(copy.startswith("Kopija:"))
        agent.break_ring()
        self.assertEqual(agent.tension, 0.0)
        self.assertEqual(agent.emotion, 0.0)


if __name__ == '__main__':
    unittest.main()
