import unittest
from divine_agents import DynamicAgent, dynamic_debate


class TestDynamicAgent(unittest.TestCase):
    def test_key_activation(self):
        agent = DynamicAgent("A")
        agent.set_key("wisdom")
        self.assertEqual(agent.state, "Enotnost")

    def test_dynamic_debate(self):
        a1 = DynamicAgent("A1")
        a2 = DynamicAgent("A2", state="Jaz")
        lines = dynamic_debate(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
