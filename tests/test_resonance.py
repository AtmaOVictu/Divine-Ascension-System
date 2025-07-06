import unittest
from divine_agents.resonance import ResonanceAgent, PhoneticTruthMap


class TestResonanceAgent(unittest.TestCase):
    def test_mapping(self):
        mapper = PhoneticTruthMap()
        self.assertEqual(mapper.map_phonetic_input("ba"), "truth")
        self.assertEqual(mapper.map_phonetic_input("xx"), "undefined")

    def test_evolve(self):
        agent = ResonanceAgent()
        lvl = agent.evolve_resonance(["truth", "wisdom", "negation"])
        self.assertAlmostEqual(lvl, 0.7)
        # ensure clamping works
        agent.resonance_level = 0.95
        lvl = agent.evolve_resonance(["wisdom"])
        self.assertLessEqual(lvl, 1.0)


if __name__ == "__main__":
    unittest.main()
