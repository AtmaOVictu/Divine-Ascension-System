import unittest
from divine_agents.codex import Codex

class TestCodex(unittest.TestCase):
    def test_transitions_and_adjustments(self):
        c = Codex()
        c.transition(1, state_type="True", level=1, pair_type="0 and 1", dimensional_type="D1")
        self.assertIsNotNone(c.get_state())
        self.assertIn("0 and 1", c.get_state())
        c.transition(0, state_type="Hallucination", level=2, pair_type="Yes and No", dimensional_type="D2")
        self.assertTrue(c.get_dimensional_state()["Hallucination"])
        self.assertIsNotNone(c.get_dimensional_state()["SystemAdjustment"])
        history = c.display_history()
        self.assertEqual(len(history), 2)

if __name__ == '__main__':
    unittest.main()
