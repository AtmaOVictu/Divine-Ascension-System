import os
import time
import unittest

from divine_agents import Agent, SubAgent

class TestAgentLogging(unittest.TestCase):
    def setUp(self):
        # Clean up potential log files from previous runs
        for fname in os.listdir('.'):
            if fname.endswith('.log') or fname.startswith('Agent1_history'):
                try:
                    os.remove(fname)
                except FileNotFoundError:
                    pass

    def test_sub_agent_addition(self):
        agent1 = Agent('Agent1')
        sub = SubAgent('SubAgent1', associated_agent=agent1)
        agent1.add_sub_agent(sub)
        self.assertIn(sub, agent1.sub_agents)
        self.assertTrue(os.path.exists(agent1.log_file))

    def test_timestamped_logging(self):
        agent1 = Agent('Agent1')
        agent1.update_emotion(0.8)
        with open(agent1.log_file, 'r') as fh:
            log_content = fh.read()
        self.assertIn('Emotion updated', log_content)
        self.assertIn(time.strftime('%Y-%m-%d', time.gmtime(agent1.timestamp)), log_content)

    def test_state_transition_logging(self):
        agent1 = Agent('Agent1')
        sub = SubAgent('SubAgent1', associated_agent=agent1)
        agent1.add_sub_agent(sub)
        agent1.update_emotion(0.9)
        agent1.transition()
        self.assertTrue(any('State transitioned to' in log for log in agent1.logs))

    def test_log_sorting_by_timestamp(self):
        agent1 = Agent('Agent1')
        agent1.update_emotion(0.7)
        agent1.transition()
        time.sleep(1)
        agent1.update_emotion(0.8)
        agent1.transition()
        sorted_logs = agent1.sort_logs()
        self.assertLessEqual(sorted_logs[0], sorted_logs[1])

    def test_action_labeling(self):
        agent1 = Agent('Agent1')
        sub = SubAgent('SubAgent1', associated_agent=agent1)
        agent1.add_sub_agent(sub)
        agent1.update_emotion(0.8)
        agent1.transition()
        agent1.log('Emotion update triggered.')
        sub.log_action('Sub-agent processed emotion update.')
        with open(agent1.log_file, 'r') as fh:
            content = fh.read()
        self.assertIn('Emotion update triggered', content)
        self.assertIn('Sub-agent processed emotion update', content)

    def test_history_file_generation(self):
        agent1 = Agent('Agent1')
        agent1.update_emotion(0.9)
        agent1.transition()
        history_file = agent1.save_history()
        self.assertTrue(os.path.exists(history_file))
        with open(history_file, 'r') as fh:
            history_content = fh.read()
        self.assertIn('State History for Agent1', history_content)

if __name__ == '__main__':
    unittest.main()
