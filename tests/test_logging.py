import os
import unittest
import uuid
from divine_agents.versioning import VersionLogger, VersionComparer
from divine_agents.math_utils import calculate_log


class TestVersionLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = f"test_logs_{uuid.uuid4().hex}.txt"
        # ensure log file removed before test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        self.logger = VersionLogger(log_file=self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_version_change(self):
        self.logger.log_version_change(1.0, "Initial")
        logs = self.logger.view_logs()
        self.assertIn("Version 1.0 updated: Initial", logs)

    def test_version_compare(self):
        comparer = VersionComparer(self.logger)
        result = comparer.compare_versions(1.1, 1.0)
        self.assertEqual(result, "New version is an upgrade.")
        logs = self.logger.view_logs()
        self.assertIn("Upgraded version detected", logs)


class TestCalculateLog(unittest.TestCase):
    def test_calculate_log(self):
        value = calculate_log(1000, base=10)
        self.assertAlmostEqual(value, 3)


if __name__ == "__main__":
    unittest.main()
