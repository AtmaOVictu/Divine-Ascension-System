import unittest
from divine_agents.ui import SoulCompassApp


class TestSoulCompassUI(unittest.TestCase):
    def test_tension_transition(self):
        app = SoulCompassApp(enable_ui=False)
        app.increase_tension(0.8)
        self.assertEqual(app.agent.state, "Jaz")

    def test_emotion_transition(self):
        app = SoulCompassApp(enable_ui=False)
        app.increase_emotion(0.6)
        # first transition should be to Jaz
        self.assertEqual(app.agent.state, "Jaz")
        app.increase_emotion(0.6)
        # second transition should move to Enotnost
        self.assertEqual(app.agent.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
