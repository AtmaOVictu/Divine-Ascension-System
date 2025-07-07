import os
import time
import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.manager import SubAgent


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


class TestLoggingAndManager(unittest.TestCase):
    def test_log_creation_and_history(self):
        agent = Agent("LogTest")
        agent.update_emotion(0.9)
        agent.transition()
        history_file = agent.save_history()
        self.assertTrue(os.path.exists(agent.log_file))
        self.assertTrue(os.path.exists(history_file))
        os.remove(agent.log_file)
        os.remove(history_file)

    def test_manager_sorting(self):
        a1 = Agent("M1")
        time.sleep(0.1)
        a2 = Agent("M2")
        manager = SubAgent()
        manager.add_agent(a2)
        manager.add_agent(a1)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual([a.name for a in sorted_agents], ["M1", "M2"])
        os.remove(a1.log_file)
        os.remove(a2.log_file)

    def test_response_logging(self):
        agent = Agent("Resp")
        agent.update_emotion(0.8)
        agent.transition()
        agent.respond("Kaj je resnica?")
        with open(agent.log_file) as file:
            content = file.read()
        self.assertIn("Response", content)
        os.remove(agent.log_file)


if __name__ == "__main__":
    unittest.main()
