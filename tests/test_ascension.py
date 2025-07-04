import unittest
from divine_agents.ascension import BodyAgent, SoulAgent, SpiritAgent


class TestBodySoulSpirit(unittest.TestCase):
    def test_body_add_transition(self):
        agent = BodyAgent()
        agent.transition("Material")
        agent.transition("Sensation")
        agent.transition("Action")
        state = agent.transition("ADD")
        self.assertEqual(state, "Expansion")

    def test_soul_add_transition(self):
        agent = SoulAgent()
        state = agent.transition("ADD")
        self.assertEqual(state, "Enlightenment")

    def test_spirit_add_transition(self):
        agent = SpiritAgent()
        state = agent.transition("ADD")
        self.assertEqual(state, "Transcendence")


if __name__ == '__main__':
    unittest.main()

