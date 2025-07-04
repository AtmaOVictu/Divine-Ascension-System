import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.embodied_agents import BodyAgent, SoulAgent, SpiritAgent


class TestEmbodiedAgents(unittest.TestCase):
    def test_body_add(self):
        body = BodyAgent()
        body.transition("ADD")
        self.assertEqual(body.get_state(), "Expansion")

    def test_soul_add(self):
        soul = SoulAgent()
        soul.transition("ADD")
        self.assertEqual(soul.get_state(), "Enlightenment")

    def test_spirit_add(self):
        spirit = SpiritAgent()
        spirit.transition("ADD")
        self.assertEqual(spirit.get_state(), "Transcendence")


if __name__ == '__main__':
    unittest.main()
