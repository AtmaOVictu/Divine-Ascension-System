import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.data import DataHarvester
from divine_agents.logger import CodeLogger
from divine_agents.interpreter import CodeInterpreter


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
        harvester = DataHarvester()
        logger = CodeLogger()
        lines = philosophical_dialogue(a1, a2, harvester=harvester, logger=logger)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertGreaterEqual(len(harvester.send_data()), 4)
        self.assertTrue(logger.analyze_history() == [])


class TestSystemUtilities(unittest.TestCase):
    def test_harvester_and_logger(self):
        agent = Agent("A")
        harvester = DataHarvester()
        logger = CodeLogger()
        harvester.collect_data(agent, "start")
        logger.log_event("error: failed action")
        self.assertEqual(len(harvester.send_data()), 1)
        self.assertTrue(logger.analyze_history())

    def test_interpreter_trigger(self):
        agent = Agent("B")
        agent.update_tension(0.9)
        interpreter = CodeInterpreter(agent)
        state = interpreter.interpret_decision([])
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
