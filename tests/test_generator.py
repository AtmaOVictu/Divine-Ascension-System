import unittest
from divine_agents import Agent, Generator


class TestGenerator(unittest.TestCase):
    def test_generator_activation(self):
        g = Generator()
        a = Agent("A")
        g.activate()
        g.stimulate(a, emotion_boost=0.6)
        self.assertIn(a.state, ("Jaz", "Enotnost"))


if __name__ == "__main__":
    unittest.main()
