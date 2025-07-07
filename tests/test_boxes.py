import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.boxes import SymbolicBox, RecursiveSymbolicBox


class TestSymbolicBox(unittest.TestCase):
    def test_initial_state_contains_zero(self):
        box = SymbolicBox(stage="∴")
        self.assertEqual(box.get_data()["initial_state"], 0)

    def test_transition_preserves_zero(self):
        box = SymbolicBox(stage="∴")
        box.transition("∆", {"info": 1})
        self.assertIn("initial_state", box.get_data())
        self.assertEqual(box.get_data()["initial_state"], 0)

    def test_recursive_unpack(self):
        main = RecursiveSymbolicBox(stage="∴", data={"a": 1})
        sub = RecursiveSymbolicBox(stage="∴", data={"b": 2})
        main.add_nested_box(sub)
        unpacked = main.unpack_knowledge()
        self.assertEqual(unpacked["nested_boxes"][0]["data"]["initial_state"], 0)


if __name__ == "__main__":
    unittest.main()
