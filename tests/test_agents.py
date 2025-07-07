import os
import time
import unittest
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


class TestLoggingAndHistory(unittest.TestCase):
    def setUp(self):
        self.agent = Agent("Logger")

    def tearDown(self):
        if os.path.exists(self.agent.log_file):
            os.remove(self.agent.log_file)
        history_file = f"{self.agent.name}_history_{self.agent.version}.txt"
        if os.path.exists(history_file):
            os.remove(history_file)

    def test_log_file_created(self):
        self.assertTrue(os.path.exists(self.agent.log_file))

    def test_history_generation(self):
        self.agent.save_history()
        history_file = f"{self.agent.name}_history_{self.agent.version}.txt"
        self.assertTrue(os.path.exists(history_file))

    def test_response_logging(self):
        self.agent.respond("Kaj je resnica?")
        with open(self.agent.log_file) as file:
            content = file.read()
        self.assertIn("Response", content)


class TestSubAgentManager(unittest.TestCase):
    def tearDown(self):
        for f in os.listdir('.'):  # clean possible files
            if f.endswith('.txt') and ('A1' in f or 'A2' in f):
                os.remove(f)

    def test_sorting_by_version(self):
        agent1 = Agent("A1")
        time.sleep(0.01)
        agent2 = Agent("A2")
        manager = SubAgent()
        manager.add_agent(agent2)
        manager.add_agent(agent1)
        sorted_agents = manager.sort_logs_by_version()
        self.assertEqual(sorted_agents[0].name, "A1")
