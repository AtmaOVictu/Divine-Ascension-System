import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import unittest
from divine_agents.agent import Agent
from divine_agents.analytics import DataHarvester, CodeLogger, CodeInterpreter


class TestAnalytics(unittest.TestCase):
    def test_harvester_collect(self):
        h = DataHarvester()
        h.collect_data({'x': 1})
        self.assertEqual(h.send_data(), [{'x': 1}])

    def test_logger(self):
        logger = CodeLogger()
        logger.log_event('error: something went wrong')
        self.assertEqual(logger.analyze_history(), ['error: something went wrong'])

    def test_interpreter_transition(self):
        agent = Agent('A')
        interpreter = CodeInterpreter(agent)
        new_state = interpreter.interpret_decision({'emotion': 0.6})
        self.assertEqual(new_state, 'Jaz')


if __name__ == '__main__':
    unittest.main()
