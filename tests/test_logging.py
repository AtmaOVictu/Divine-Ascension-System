import unittest
import os
import sys
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.agent import Agent, SubAgent


class TestAgentSubAgentLogging(unittest.TestCase):
    def tearDown(self):
        # cleanup generated files
        for fname in os.listdir('.'):
            if fname.endswith('_log.txt') or fname.startswith('Agent1_history'):
                try:
                    os.remove(fname)
                except FileNotFoundError:
                    pass

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

        with open(agent1.log_file, 'r', encoding='utf-8') as file:
            log_content = file.read()
            self.assertIn("Emotion updated", log_content)
            today = time.strftime('%Y-%m-%d', time.gmtime(agent1.timestamp))
            self.assertIn(today, log_content)

    def test_state_transition_logging(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.9)
        agent1.transition()

        self.assertTrue(sub_agent1.logs)
        self.assertIn("Sub-agent", agent1.logs[0])
        self.assertIn("State transitioned", agent1.logs[-1])

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
        self.assertTrue(sorted_logs[0].startswith(sorted_logs[0].split(' - ')[0]))
        self.assertTrue(len(sorted_logs) >= 1)

    def test_action_labeling(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.8)
        agent1.transition()

        agent1.log("Emotion update triggered.")
        sub_agent1.log_action("Sub-agent processed emotion update.")

        with open(agent1.log_file, 'r', encoding='utf-8') as file:
            log_content = file.read()
            self.assertIn("Emotion update triggered", log_content)
            self.assertIn("Sub-agent processed emotion update", log_content)

    def test_history_file_generation(self):
        agent1 = Agent("Agent1")
        agent1.update_emotion(0.9)
        agent1.transition()

        history_file = agent1.save_history()
        self.assertTrue(os.path.exists(history_file))

        with open(history_file, 'r', encoding='utf-8') as file:
            history_content = file.read()
            self.assertIn("State History for Agent1", history_content)


if __name__ == '__main__':
    unittest.main()
