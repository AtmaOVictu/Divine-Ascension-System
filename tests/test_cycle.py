import unittest

from divine_agents.cycle_model import CycleModel


class TestCycleModel(unittest.TestCase):
    def test_color_changes_at_threshold(self):
        model = CycleModel()
        model.angle = 59
        angle, color, changed = model.step()
        self.assertEqual(angle, 60)
        self.assertEqual(color, "red")
        self.assertTrue(changed)


if __name__ == "__main__":
    unittest.main()
