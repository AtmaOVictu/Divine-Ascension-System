import os
import time
import unittest

from divine_agents.agent import Agent, SubAgent


class TestAgentSubAgentLogging(unittest.TestCase):
    def tearDown(self):
        # Cleanup created files
        for fname in os.listdir('.'):
            if fname.endswith('_log.txt') or fname.startswith('Agent1_history'):
                os.remove(fname)

    def test_sub_agent_addition(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)
        self.assertIn(sub_agent1, agent1.sub_agents)
        sub_agent1.log_action("Sub-agent added.")
        self.assertTrue(os.path.exists(agent1.log_file))

    def test_timestamped_logging(self):
        agent1 = Agent("Agent1")
        sub_agent1 = SubAgent("SubAgent1", associated_agent=agent1)
        agent1.add_sub_agent(sub_agent1)

        agent1.update_emotion(0.8)
        time.sleep(0.1)

        with open(agent1.log_file, 'r') as file:
            log_content = file.read()
            self.assertIn("Emotion updated", log_content)
            # Ensure timestamp exists (approximate check)
            first_part = log_content.split("::", 1)[0]
            self.assertTrue(float(first_part) <= time.time())

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
        time.sleep(0.1)
        agent1.update_emotion(0.8)
        agent1.transition()
        sorted_logs = sub_agent1.sort_logs()
        self.assertLessEqual(float(sorted_logs[0].split("::",1)[0]), float(sorted_logs[1].split("::",1)[0]))

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
        self.assertIn("Sub-agent processed emotion update", " ".join(sub_agent1.logs))

    def test_history_file_generation(self):
        agent1 = Agent("Agent1")
        agent1.update_emotion(0.9)
        agent1.transition()
        agent1.save_history()
        history_file = f"{agent1.name}_history_{agent1.version - 1}.txt"
        self.assertTrue(os.path.exists(history_file))
        with open(history_file, 'r') as file:
            history_content = file.read()
            self.assertIn("State History for Agent1", history_content)


if __name__ == '__main__':
    unittest.main()
