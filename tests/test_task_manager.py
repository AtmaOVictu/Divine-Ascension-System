import unittest
from divine_agents.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_close_branch_progress(self):
        tm = TaskManager()
        tm.add_open_branch("k1")
        tm.close_branch("k1")
        self.assertEqual(tm.points, 0)
        self.assertIn("k1", tm.closed_branches)


if __name__ == "__main__":
    unittest.main()
