import unittest
import uuid

from divine_agents.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_and_close_branch(self):
        manager = TaskManager()
        bid = manager.add_open_branch("Krak A")
        self.assertIn(bid, manager.open_branches)
        self.assertTrue(manager.close_branch(bid))
        self.assertEqual(manager.open_branches[bid]["status"], "closed")

    def test_check_for_progress(self):
        manager = TaskManager()
        b1 = manager.add_open_branch("A")
        b2 = manager.add_open_branch("A")
        manager.close_branch(b1)
        manager.close_branch(b2)
        self.assertTrue(manager.check_for_progress())

    def test_find_related_branches(self):
        manager = TaskManager()
        b1 = manager.add_open_branch("Relacija")
        b2 = manager.add_open_branch("Relacija")
        related = manager.find_related_branches(b1)
        self.assertIn(b2, related)


if __name__ == "__main__":
    unittest.main()
