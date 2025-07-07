import os
import tempfile
import time
import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.subagent_manager import SubAgentManager


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

    def test_log_creation_and_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            agent = Agent("LogA", log_dir=tmp)
            agent.update_emotion(0.9)
            agent.transition()
            agent.respond("Kaj je resnica?")
            log_path = agent.log_file
            hist_path = agent.save_history()
            self.assertTrue(os.path.exists(log_path))
            self.assertTrue(os.path.exists(hist_path))
            with open(log_path, "r") as fh:
                content = fh.read()
            self.assertIn("Emotion updated", content)
            self.assertIn("Response:", content)

    def test_manager_sorting(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = SubAgentManager()
            a1 = Agent("A1", log_dir=tmp)
            time.sleep(1)
            a2 = Agent("A2", log_dir=tmp)
            m.add_agent(a2)
            m.add_agent(a1)
            sorted_agents = m.sort_logs_by_version()
            self.assertEqual(sorted_agents[0], a1)



if __name__ == '__main__':
    unittest.main()
