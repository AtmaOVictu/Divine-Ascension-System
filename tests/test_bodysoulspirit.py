import unittest
from divine_agents.body_soul_spirit import BodyAgent, SoulAgent, SpiritAgent


class TestBodySoulSpirit(unittest.TestCase):
    def test_body_add(self):
        body = BodyAgent()
        body.transition("ADD")
        self.assertEqual(body.get_state(), "Expansion")

    def test_soul_add(self):
        soul = SoulAgent()
        soul.transition("DODAJ")
        self.assertEqual(soul.get_state(), "Enlightenment")

    def test_spirit_add(self):
        spirit = SpiritAgent()
        spirit.transition("ADD")
        self.assertEqual(spirit.get_state(), "Transcendence")


if __name__ == "__main__":
    unittest.main()
