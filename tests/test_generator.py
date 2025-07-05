import unittest
from divine_agents import Agent, Generator


class TestGenerator(unittest.TestCase):
    def test_activation_and_transition(self):
        agent = Agent("G")
        gen = Generator()
        gen.activate(0.8)
        new_state = gen.energize(agent)
        self.assertEqual(new_state, "Jaz")

    def test_no_activation(self):
        agent = Agent("G")
        gen = Generator()
        state = gen.energize(agent)
        self.assertEqual(state, "Ego")


if __name__ == "__main__":
    unittest.main()
