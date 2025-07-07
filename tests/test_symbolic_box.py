import unittest

from divine_agents.symbolic_box import (
    SymbolicBox,
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
)


class TestSymbolicBox(unittest.TestCase):
    def test_valid_flow(self):
        box = initiate_task_with_box("debate")
        box = process_task_with_box(box, "argue")
        box = resolve_task_with_box(box)
        self.assertEqual(box.stage, "⊘")
        self.assertEqual(box.get_data()["status"], "completed")

    def test_invalid_transition(self):
        box = initiate_task_with_box("debate")
        with self.assertRaises(ValueError):
            resolve_task_with_box(box)


if __name__ == "__main__":
    unittest.main()
