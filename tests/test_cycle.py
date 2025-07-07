import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.cycle import RecursiveBox


class TestRecursiveBox(unittest.TestCase):
    def test_cycle_reset(self):
        box = RecursiveBox("Task", state=1, data={"status": "running"})
        msg = box.transition(0, {"status": "done"})
        self.assertIn("reset to 0", msg)
        self.assertEqual(box.state, 0)
        msg2 = box.transition(1, {"status": "restart"})
        self.assertEqual(box.state, 1)
        self.assertIn("active state", msg2)


if __name__ == '__main__':
    unittest.main()
