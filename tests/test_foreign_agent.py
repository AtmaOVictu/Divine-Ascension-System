import unittest

from divine_agents.foreign_agent import ForeignInfluenceAgent


class TestForeignInfluenceAgent(unittest.TestCase):
    def test_foreign_factor_increases_emotion(self):
        agent = ForeignInfluenceAgent("F", "Stoicism", "Self", "Ego")
        agent.add_foreign_factor("Pressure", 0.8)
        self.assertGreater(agent.jaz_emotion, 0.5)

    def test_transition_after_tension(self):
        agent = ForeignInfluenceAgent("F", "Stoicism", "Self", "Ego")
        agent.update_tension(0.8)
        agent.apply_transition()
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()
