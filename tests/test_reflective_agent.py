import unittest
from divine_agents.reflective_agent import ReflectiveAgent
from divine_agents.dynamic_dialogue import dynamic_philosophical_dialogue


class TestReflectiveAgent(unittest.TestCase):
    def test_belief_update(self):
        agent = ReflectiveAgent("A")
        agent.update_emotion(0.6)
        belief = agent.update_belief("Razmišljam o tvojem pogledu.")
        self.assertIn("ABSOLUTNA", belief)

    def test_transition_with_emotion(self):
        agent = ReflectiveAgent("A")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_dialogue(self):
        a1 = ReflectiveAgent("A1")
        a2 = ReflectiveAgent("A2", state="Jaz")
        lines = dynamic_philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja" in line for line in lines))
        self.assertTrue(any("Enotnost" in line or "Jaz" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
