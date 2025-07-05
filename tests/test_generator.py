import unittest
from divine_agents import Agent, Generator


class TestGenerator(unittest.TestCase):
    def test_generator_triggers_transition(self):
        agent = Agent("A")
        gen = Generator()
        gen.activate(power=1.0)
        gen.apply_to_agent(agent)
        self.assertEqual(agent.state, "Jaz")

    def test_generator_inactive(self):
        agent = Agent("A")
        gen = Generator(power=1.0)
        gen.apply_to_agent(agent)
        self.assertEqual(agent.state, "Ego")


if __name__ == "__main__":
    unittest.main()
