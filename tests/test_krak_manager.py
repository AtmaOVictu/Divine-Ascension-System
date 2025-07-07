import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.krak_manager import KrakManager, Krak


class TestKrakManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = KrakManager("https://github.com/example/repo", "https://vercel.app/api")

    def test_add_krak(self):
        krak = Krak("Sample", "condition")
        self.manager.add_krak(krak)
        self.assertEqual(len(self.manager.kraks), 1)
        self.assertEqual(self.manager.kraks[0].status, "pending")

    def test_distribute_krak(self):
        krak = Krak("ToDistribute", "condition")
        self.manager.add_krak(krak)
        with patch("divine_agents.krak_manager.random.random", return_value=0.9):
            with patch.object(self.manager.vercel_handler, "trigger_task", return_value="triggered"):
                with patch.object(self.manager.github_handler, "update_task_status", return_value="updated"):
                    msg = self.manager.distribute_krak()
        self.assertIn("Distributed", msg)
        self.assertEqual(self.manager.kraks[0].status, "in-progress")


if __name__ == "__main__":
    unittest.main()
