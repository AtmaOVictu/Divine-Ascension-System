import unittest
from divine_agents.state_box import StateBox


class TestStateBox(unittest.TestCase):
    def test_initial_state(self):
        box = StateBox(0)
        self.assertEqual(box.state, 0)
        self.assertEqual(box.data["status"], "initialized")

    def test_transition_valid(self):
        box = StateBox(0)
        box.transition(1, {"status": "active"})
        self.assertEqual(box.state, 1)
        self.assertEqual(box.data["status"], "active")
        self.assertTrue(box.history)

    def test_transition_invalid(self):
        box = StateBox(0)
        with self.assertRaises(ValueError):
            box.transition(2)

    def test_protection(self):
        box = StateBox(0)
        box.set_protection(True)
        with self.assertRaises(PermissionError):
            box.update_data({"x": 1})


if __name__ == "__main__":
    unittest.main()
