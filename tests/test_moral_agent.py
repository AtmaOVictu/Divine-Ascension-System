import unittest
from divine_agents import MoralAgent, moral_dialogue


class TestMoralAgent(unittest.TestCase):
    def test_moral_transition(self):
        agent = MoralAgent("M")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_moral_decision(self):
        a1 = MoralAgent("A1", ethics="deontology")
        decision = a1.moral_decision([])
        self.assertIn("Follow the rule", decision)

    def test_moral_dialogue(self):
        a1 = MoralAgent("A1")
        a2 = MoralAgent("A2", state="Jaz")
        lines = moral_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
