import os
import time
import unittest

from divine_agents import Agent, SubAgent
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

    def test_log_creation(self):
        agent = Agent("LogTester")
        self.assertTrue(os.path.exists(agent.log_file))

    def test_subagent_sorting(self):
        a1 = Agent("S1")
        time.sleep(1)
        a2 = Agent("S2")
        manager = SubAgent()
        manager.add_agent(a2)
        manager.add_agent(a1)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual([a1, a2], sorted_agents)

    def test_response_logging(self):
        agent = Agent("Resp")
        agent.respond("Kaj je resnica?")
        with open(agent.log_file) as f:
            logs = f.read()
        self.assertIn("Response:", logs)

    def test_history_file_generation(self):
        agent = Agent("Hist")
        agent.update_tension(0.8)
        agent.transition()
        agent.save_history()
        history_file = f"{agent.name}_history_{agent.version}.txt"
        self.assertTrue(os.path.exists(history_file))


if __name__ == '__main__':
    unittest.main()
