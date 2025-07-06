import unittest
import json
import os
import tempfile

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.logger import ChangeLogger


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Čustveni odziv", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_logger_records_changes(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            path = tmp.name
        try:
            agent = Agent("L", log_file=path)
            agent.update_emotion(0.6)
            agent.transition()
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.assertGreater(len(data), 0)
        finally:
            os.remove(path)


if __name__ == '__main__':
    unittest.main()
