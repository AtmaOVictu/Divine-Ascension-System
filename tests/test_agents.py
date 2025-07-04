import unittest
import os
import sys

# Ensure the project root is on the import path when tests are executed
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.utils import access_local_disk, log_history


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

    def test_history_logging(self):
        tmp_log = os.path.join(os.path.dirname(__file__), "temp_history.txt")
        try:
            agent = Agent("A", log_path=tmp_log)
            agent.update_tension(0.9)
            agent.transition()
            with open(tmp_log, "r", encoding="utf-8") as fh:
                data = fh.read()
            self.assertIn("transitioned", data)
        finally:
            if os.path.exists(tmp_log):
                os.remove(tmp_log)

    def test_access_local_disk(self):
        tmp_dir = os.path.dirname(__file__)
        contents = access_local_disk(tmp_dir)
        self.assertIn("test_agents.py", contents)


if __name__ == '__main__':
    unittest.main()
