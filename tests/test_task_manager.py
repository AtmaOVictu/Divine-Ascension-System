import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from divine_agents.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_and_close_branch(self):
        manager = TaskManager()
        bid = manager.add_open_branch("Krak A")
        self.assertIn(bid, manager.open_branches)
        manager.close_branch(bid)
        self.assertEqual(manager.open_branches[bid]["status"], "closed")
        # history is cleared when all branches are closed
        self.assertEqual(manager.history, [])

    def test_find_related(self):
        manager = TaskManager()
        b1 = manager.add_open_branch("Krak A")
        b2 = manager.add_open_branch("Krak A")
        related = manager.find_related_branches(b1)
        self.assertIn(b2, related)


if __name__ == "__main__":
    unittest.main()
