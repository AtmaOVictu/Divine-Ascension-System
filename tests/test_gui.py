import sys
import unittest
from unittest.mock import patch

from divine_agents.agent import Agent
from divine_agents.gui import TransitionWindow, launch_gui


class DummyLabel:
    def __init__(self):
        self.text = ""

    def config(self, text: str):
        self.text = text


class TestTransitionWindow(unittest.TestCase):
    def test_transition_updates_label(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        window = TransitionWindow([agent])
        label = DummyLabel()
        window._on_transition(agent, label)
        self.assertEqual(agent.state, "Jaz")
        self.assertIn("Jaz", label.text)

    def test_launch_gui_version(self):
        self.assertGreaterEqual(sys.version_info[:2], (3, 6))
        with patch.object(TransitionWindow, "run", return_value=None) as mock_run:
            launch_gui([Agent("B")])
            mock_run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
