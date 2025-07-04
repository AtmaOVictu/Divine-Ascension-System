import unittest
from divine_agents.window import TransitionWindow


class TestTransitionWindow(unittest.TestCase):
    def test_headless_activation(self):
        tw = TransitionWindow(headless=True)
        tw.activate_transition()
        self.assertTrue(tw.transition_active)
        self.assertTrue(tw.new_window_created)
        self.assertIn("osve", tw.label_text)


if __name__ == "__main__":
    unittest.main()
