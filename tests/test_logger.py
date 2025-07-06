import os
import tempfile
import unittest

from divine_agents.logger import VersionLogger, VersionComparer


class TestLogger(unittest.TestCase):
    def test_log_version_change(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            logger = VersionLogger(tmp.name)
            logger.log_version_change(1.0, "Initial release")
            contents = logger.view_logs()
        self.assertIn("Version 1.0 updated: Initial release", contents)
        os.remove(tmp.name)

    def test_version_comparer_upgrade(self):
        with tempfile.NamedTemporaryFile(delete=True) as tmp:
            logger = VersionLogger(tmp.name)
            comparer = VersionComparer(logger)
            result = comparer.compare_versions(1.2, 1.1)
            self.assertEqual(result, "New version is an upgrade.")
