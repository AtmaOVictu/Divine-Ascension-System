import unittest
from divine_agents.spiritual_rebirth import SpiritualAgent, philosophical_debate


class TestSpiritualRebirth(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = SpiritualAgent("A")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_tension(self):
        agent = SpiritualAgent("B", state="Jaz")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_dialogue_contains_enotnost(self):
        a1 = SpiritualAgent("A1")
        a2 = SpiritualAgent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
