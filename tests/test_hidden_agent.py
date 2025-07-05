import unittest
from divine_agents.hidden_agent import HiddenModerator


class TestHiddenModerator(unittest.TestCase):
    def test_activation(self):
        mod = HiddenModerator(name="Mod")
        mod.evaluate_state(tension=0.6, emotion=0.4)
        self.assertEqual(mod.state, "active")
        self.assertTrue(mod.activation_triggered)

    def test_reveal(self):
        mod = HiddenModerator(name="Mod")
        mod.activate_moderator()
        mod.reveal_moderator()
        self.assertEqual(mod.state, "revealed")
        self.assertEqual(mod.history[-1], "revealed")


if __name__ == "__main__":
    unittest.main()
