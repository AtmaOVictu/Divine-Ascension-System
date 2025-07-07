import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.box import RecursiveSymbolicBox


class TestRecursiveSymbolicBox(unittest.TestCase):
    def test_transition_and_rollback(self):
        box = RecursiveSymbolicBox(stage="∴", data={"task": "start"})
        box.transition("∆", {"step": 1})
        self.assertEqual(box.stage, "∆")
        self.assertIn("step", box.get_data())
        box.rollback()
        self.assertEqual(box.stage, "∴")
        self.assertNotIn("step", box.get_data())


if __name__ == "__main__":
    unittest.main()
