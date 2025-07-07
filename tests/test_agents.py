import os
import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.sub_agent import SubAgent


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

    def test_agent_logging(self):
        agent = Agent("LogA")
        agent.update_emotion(0.9)
        agent.transition()
        self.assertTrue(os.path.exists(agent.log_file))

    def test_sub_agent_sorting(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        manager = SubAgent()
        manager.add_agent(a1)
        manager.add_agent(a2)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual(len(sorted_agents), 2)

    def test_agent_response_and_log(self):
        agent = Agent("A3")
        agent.update_emotion(0.8)
        agent.transition()
        response = agent.respond("Kaj je resnica?")
        with open(agent.log_file) as f:
            log_content = f.read()
        self.assertIn(response, log_content)

    def test_agent_history_file(self):
        agent = Agent("A4")
        agent.update_emotion(0.9)
        agent.transition()
        agent.save_history()
        history_file = f"{agent.name}_history_{agent.version}.txt"
        self.assertTrue(os.path.exists(history_file))


if __name__ == '__main__':
    unittest.main()
