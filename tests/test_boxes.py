import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.box import SymbolicBox, RecursiveSymbolicBox


class TestSymbolicBox(unittest.TestCase):
    def test_initial_state(self):
        box = SymbolicBox(stage="∴")
        self.assertIn("initial_state", box.get_data())
        self.assertEqual(box.get_data()["initial_state"], 0)

    def test_transition(self):
        box = SymbolicBox(stage="∴")
        box.transition("∆", {"progress": True})
        self.assertEqual(box.stage, "∆")
        self.assertEqual(box.get_data()["initial_state"], 0)


class TestRecursiveSymbolicBox(unittest.TestCase):
    def test_nested_box_contains_zero(self):
        parent = RecursiveSymbolicBox(stage="∴")
        child = RecursiveSymbolicBox(stage="∴")
        parent.add_nested_box(child)
        data = parent.unpack_knowledge()
        self.assertEqual(data["data"]["initial_state"], 0)
        self.assertEqual(data["nested_boxes"][0]["data"]["initial_state"], 0)


if __name__ == "__main__":
    unittest.main()
