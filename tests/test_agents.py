import os
import time
import tempfile
import unittest

from divine_agents import Agent, SubAgent, philosophical_dialogue


class TestAgentSystem(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_transition_thresholds(self):
        agent = Agent("A", log_dir=self.tmp.name)
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_log_creation(self):
        agent = Agent("B", log_dir=self.tmp.name)
        self.assertTrue(os.path.exists(agent.log_file))

    def test_subagent_sorting(self):
        a1 = Agent("A1", log_dir=self.tmp.name)
        time.sleep(0.1)
        a2 = Agent("A2", log_dir=self.tmp.name)
        manager = SubAgent()
        manager.add_agent(a2)
        manager.add_agent(a1)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual(sorted_agents[0].version, a1.version)

    def test_response_logging_and_history(self):
        agent = Agent("C", log_dir=self.tmp.name)
        agent.update_emotion(0.6)
        agent.transition()
        agent.respond("Kaj je resnica?")
        agent.save_history()

        with open(agent.log_file, "r", encoding="utf-8") as file:
            log = file.read()
        self.assertIn("Emotion updated", log)
        self.assertIn("State transitioned", log)
        self.assertIn("Response:", log)

        history_path = os.path.join(self.tmp.name, f"{agent.name}_history_{agent.version}.txt")
        self.assertTrue(os.path.exists(history_path))

    def test_dialogue(self):
        a1 = Agent("D1", log_dir=self.tmp.name)
        a2 = Agent("D2", state="Jaz", log_dir=self.tmp.name)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
