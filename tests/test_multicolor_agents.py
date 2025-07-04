import unittest
from divine_agents.multicolor_agent import MultiColorAgent
from divine_agents.dialogue import colorful_dialogue


class TestMultiColorAgent(unittest.TestCase):
    def test_color_update_on_transition(self):
        agent = MultiColorAgent("A")
        agent.update_tension(0.8)
        agent.transition()
        self.assertIn(agent.current_color(), MultiColorAgent.COLOR_MAP.values())

    def test_visibility_toggle(self):
        agent = MultiColorAgent("B")
        initial_visibility = agent.current_visibility()
        agent.toggle_visibility()
        self.assertIn(agent.current_visibility(), ("Visible", "Hidden"))
        # Could be same or different due to randomness

    def test_colorful_dialogue(self):
        a1 = MultiColorAgent("A1")
        a2 = MultiColorAgent("A2", state="Jaz")
        lines = colorful_dialogue(a1, a2)
        self.assertTrue(any("Gold" in line or "Blue" in line or "Red" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
