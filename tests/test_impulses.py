import unittest
from divine_agents.agent import Agent
from divine_agents.impulses import Volja, Vera, Vzgib


class TestImpulses(unittest.TestCase):
    def test_volja_triggers_transition(self):
        agent = Agent("B")
        volja = Volja()
        volja.aktivacija()
        volja.apply(agent)
        self.assertEqual(agent.state, "Jaz")

    def test_vzgib_combined(self):
        agent = Agent("C")
        vzgib = Vzgib()
        messages = vzgib.izvajanje(agent)
        self.assertIn("Volja je aktivirana", messages[0])
        self.assertEqual(agent.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
