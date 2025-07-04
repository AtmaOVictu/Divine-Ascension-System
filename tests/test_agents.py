import os
import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def setUp(self):
        if os.path.exists("history_log.txt"):
            os.remove("history_log.txt")

    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion(0.6, "joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veseljem", reply)
        self.assertIn("relativna", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        with open("history_log.txt", "r", encoding="utf-8") as fh:
            log = fh.read()
        self.assertIn("A1 transitioned", log)


if __name__ == '__main__':
    unittest.main()
