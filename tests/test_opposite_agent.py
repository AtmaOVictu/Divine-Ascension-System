import unittest
from divine_agents import Agent, OppositeSeekingAgent

class TestOppositeAgent(unittest.TestCase):
    def test_opposition_generation(self):
        base = Agent("Base")
        opp = OppositeSeekingAgent("Opp")
        reply = opp.respond_to(base, "Kaj je resnica?")
        self.assertIn("Nasprotje", reply)

    def test_opposite_transition(self):
        opp = OppositeSeekingAgent("Opp")
        opp.update_tension(0.8)
        state = opp.transition()
        self.assertEqual(state, "Jaz")

if __name__ == '__main__':
    unittest.main()
