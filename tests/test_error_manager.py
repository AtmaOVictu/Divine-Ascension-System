import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.error_manager import ErrorManager


class TestErrorManager(unittest.TestCase):
    def test_log_and_resolve(self):
        manager = ErrorManager()
        manager.log_error("Test failure", "Test Error")
        self.assertEqual(len(manager.potential_issues), 1)
        resolved = manager.resolve_error("Test failure")
        self.assertTrue(resolved)
        self.assertEqual(len(manager.potential_issues), 0)


if __name__ == '__main__':
    unittest.main()
