import unittest
import time
from pathlib import Path

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.manager import SubAgentManager


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
        agent = Agent("LogTest")
        agent.update_emotion(0.9)
        agent.transition()
        agent.save_history()
        self.assertTrue(agent.log_file.exists())
        history_path = Path(f"{agent.name}_history_{agent.version}.txt")
        self.assertTrue(history_path.exists())
        # Clean up
        agent.log_file.unlink(missing_ok=True)
        history_path.unlink(missing_ok=True)

    def test_subagent_sorting(self):
        manager = SubAgentManager()
        a1 = Agent("First")
        time.sleep(1)
        a2 = Agent("Second")
        manager.add_agent(a2)
        manager.add_agent(a1)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual(sorted_agents[0].name, "First")
        self.assertEqual(sorted_agents[1].name, "Second")


if __name__ == '__main__':
    unittest.main()
