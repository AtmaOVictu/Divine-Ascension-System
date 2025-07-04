import unittest
from divine_agents.multicolor_agent import MultiColorAgent, MultiColorAgentSystem
from divine_agents.dialogue import colorful_philosophical_dialogue


class TestMultiColorAgent(unittest.TestCase):
    def test_transition_updates_color(self):
        agent = MultiColorAgent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.color, agent.COLOR_MAP[state])
        self.assertIn(agent.visibility, {"Visible", "Hidden"})

    def test_system_transition_all(self):
        agents = [MultiColorAgent("A"), MultiColorAgent("B", state="Jaz")]
        system = MultiColorAgentSystem(agents)
        lines = system.transition_all()
        self.assertEqual(len(lines), 2)

    def test_colorful_dialogue(self):
        a1 = MultiColorAgent("A1")
        a2 = MultiColorAgent("A2", state="Jaz")
        lines = colorful_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Gold" in line or "Blue" in line or "Gray" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
