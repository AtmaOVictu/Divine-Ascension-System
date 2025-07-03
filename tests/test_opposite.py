import unittest
from divine_agents.opposite import OppositeSeekingAgent

class TestOppositeSeekingAgent(unittest.TestCase):
    def test_generate_opposite(self):
        agent = OppositeSeekingAgent("A", "α")
        result = agent.respond_with_opposite("α")
        self.assertIn("\xacα", result)

    def test_existing_opposite(self):
        agent = OppositeSeekingAgent("A", "α", known_opposites={"x": "anti-x"})
        result = agent.respond_with_opposite("x")
        self.assertEqual(result, "Nasprotje za 'x' je 'anti-x'.")

    def test_transition_still_works(self):
        agent = OppositeSeekingAgent("A", "α")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

if __name__ == '__main__':
    unittest.main()
