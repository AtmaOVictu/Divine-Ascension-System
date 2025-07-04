import unittest
from divine_agents.multi_color_agent import MultiColorAgent


class TestMultiColorAgent(unittest.TestCase):
    def test_color_changes_on_transition(self):
        agent = MultiColorAgent("MC")
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(agent.current_color(), MultiColorAgent.COLORS["Jaz"])

    def test_visibility_toggle(self):
        agent = MultiColorAgent("MC")
        initial = agent.current_visibility()
        agent.toggle_visibility()
        self.assertIn(agent.current_visibility(), ("Visible", "Hidden"))
        self.assertNotEqual(initial, None)


if __name__ == "__main__":
    unittest.main()
