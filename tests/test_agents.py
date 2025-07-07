import os
import sys
import time
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.subagent import SubAgentManager


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
        agent = Agent("LogTester")
        agent.update_emotion(0.9)
        agent.transition()
        agent.save_history()
        self.assertTrue(os.path.exists(agent.log_file))
        history_path = f"{agent.name}_history_{agent.version}.txt"
        self.assertTrue(os.path.exists(history_path))

    def test_subagent_sorting(self):
        manager = SubAgentManager()
        a1 = Agent("S1")
        time.sleep(0.01)
        a2 = Agent("S2")
        manager.add_agent(a2)
        manager.add_agent(a1)
        sorted_agents = manager.sort_by_timestamp()
        self.assertEqual(sorted_agents[0].name, "S1")


if __name__ == '__main__':
    unittest.main()
