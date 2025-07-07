import unittest
from divine_agents.box import SymbolicBox, RecursiveSymbolicBox


class TestSymbolicBox(unittest.TestCase):
    def test_initial_state(self):
        box = SymbolicBox(stage="∴")
        self.assertEqual(box.data["initial_state"], 0)

    def test_update_preserves_zero(self):
        box = SymbolicBox(stage="∴")
        box.update_data({"info": 1})
        self.assertEqual(box.data["initial_state"], 0)
        self.assertEqual(box.data["info"], 1)

    def test_transition_validation(self):
        box = SymbolicBox(stage="∴")
        box.transition("∆", {"step": 1})
        self.assertEqual(box.stage, "∆")
        with self.assertRaises(ValueError):
            box.transition("∴", {})


class TestRecursiveSymbolicBox(unittest.TestCase):
    def test_nested_boxes_transition(self):
        parent = RecursiveSymbolicBox(stage="∴")
        child = SymbolicBox(stage="∴")
        parent.add_nested_box(child)
        parent.transition("∆", {"status": "processing"})
        self.assertEqual(parent.stage, "∆")
        self.assertEqual(child.stage, "∆")
        self.assertEqual(parent.data["initial_state"], 0)
        self.assertEqual(child.data["initial_state"], 0)


if __name__ == "__main__":
    unittest.main()
