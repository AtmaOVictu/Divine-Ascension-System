import unittest
from divine_agents.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_branch_progression(self):
        tm = TaskManager()
        tm.add_open_branch("Krake A")
        tm.close_branch("Krake A")
        self.assertIn("Krake B", tm.open_branches)

if __name__ == "__main__":
    unittest.main()
