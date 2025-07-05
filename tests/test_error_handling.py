import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.error_handling import SimpleErrorLogger, DateErrorLogger


class TestErrorLogging(unittest.TestCase):
    def test_simple_logger(self):
        logger = SimpleErrorLogger()
        logger.log_error("Napaka pri nalaganju")
        self.assertIn("Napaka pri nalaganju", logger.errors)

    def test_date_logger(self):
        logger = DateErrorLogger()
        logger.log_error("Napaka")
        self.assertTrue(logger.errors and "Napaka" in logger.errors[0])


if __name__ == '__main__':
    unittest.main()
