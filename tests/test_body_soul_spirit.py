import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.body_soul_spirit import BodyAgent, SoulAgent, SpiritAgent


class TestBodySoulSpiritAgents(unittest.TestCase):
    def test_body_add_transition(self):
        body = BodyAgent()
        body.transition("ADD")
        self.assertEqual(body.get_state(), "Expansion")

    def test_soul_add_transition(self):
        soul = SoulAgent()
        soul.transition("DODAJ")
        self.assertEqual(soul.get_state(), "Enlightenment")

    def test_spirit_add_transition(self):
        spirit = SpiritAgent()
        spirit.transition("ADD")
        self.assertEqual(spirit.get_state(), "Transcendence")


if __name__ == "__main__":
    unittest.main()
