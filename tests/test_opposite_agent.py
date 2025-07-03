import unittest
from divine_agents.opposite_agent import OppositeSeekingAgent


class TestOppositeSeekingAgent(unittest.TestCase):
    def test_generate_opposite_when_none_available(self):
        agent = OppositeSeekingAgent("A", symbol="α")
        generated = agent.find_or_generate_opposite()
        self.assertEqual(generated, "¬α")

    def test_use_environment_symbol_as_opposite(self):
        agent = OppositeSeekingAgent("B", symbol="α")
        generated = agent.find_or_generate_opposite(["β", "γ"])
        self.assertEqual(generated, "β")

    def test_transition_updates_state_and_opposite(self):
        agent = OppositeSeekingAgent("C", symbol="α")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertIsNotNone(agent.opposite_symbol)


if __name__ == "__main__":
    unittest.main()
