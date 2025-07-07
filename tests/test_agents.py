import unittest
import os
import time
from divine_agents.agent import Agent, SubAgent
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


class TestAgentLogging(unittest.TestCase):
    def test_sub_agent_addition(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)

        agent1.add_sub_agent(sub_agent1)

        self.assertIn(sub_agent1, agent1.sub_agents)
        sub_agent1.log("Sub-agent added.")
        self.assertTrue(os.path.exists(agent1.log_file))

    def test_timestamped_logging(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.8)
        time.sleep(1)

        with open(agent1.log_file, 'r') as file:
            log_content = file.read()
            self.assertIn("Emotion updated", log_content)
            self.assertIn(time.strftime('%Y-%m-%d', time.gmtime(agent1.timestamp)), log_content)

    def test_state_transition_logging(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.9)
        agent1.transition()

        self.assertTrue(sub_agent1.logs)
        self.assertIn("State transitioned to", sub_agent1.logs[-1])

    def test_log_sorting_by_timestamp(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.7)
        agent1.transition()
        time.sleep(1)
        agent1.update_emotion(0.8)
        agent1.transition()

        sorted_logs = sub_agent1.sort_logs()

        self.assertTrue(sorted_logs[0].startswith("Emotion updated"))
        self.assertTrue(sorted_logs[1].startswith("State transitioned"))

    def test_action_labeling(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.8)
        agent1.transition()

        agent1.log("Emotion update triggered.")
        sub_agent1.log_action("Sub-agent processed emotion update.")

        with open(agent1.log_file, 'r') as file:
            log_content = file.read()
            self.assertIn("Emotion update triggered", log_content)
            self.assertIn("Sub-agent processed emotion update", log_content)

    def test_history_file_generation(self):
        agent1 = Agent("Agent1")
        agent1.update_emotion(0.9)
        agent1.transition()

        file_name = agent1.save_history()
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            history_content = file.read()
            self.assertIn("State History for Agent1", history_content)


if __name__ == '__main__':
    unittest.main()
