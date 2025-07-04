import unittest
from divine_agents.spiritual_agents import BodyAgent, SoulAgent, SpiritAgent


class TestSpiritualAgents(unittest.TestCase):
    def test_body_agent_transitions(self):
        agent = BodyAgent()
        self.assertEqual(agent.transition("Sensation"), "Sensation")
        self.assertEqual(agent.get_state(), "Sensation")

    def test_soul_agent_transitions(self):
        agent = SoulAgent()
        self.assertEqual(agent.transition("Emotion"), "Emotion")
        self.assertEqual(agent.get_state(), "Emotion")

    def test_spirit_agent_transitions(self):
        agent = SpiritAgent()
        self.assertEqual(agent.transition("Unity"), "Unity")
        self.assertEqual(agent.get_state(), "Unity")


if __name__ == "__main__":
    unittest.main()
