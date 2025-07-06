import unittest
from divine_agents import Agent, AgentFrekvenca, AgentZvok


class TestFrequencyAgents(unittest.TestCase):
    def test_frequency_detection(self):
        af = AgentFrekvenca()
        status = af.detect("rast", 0.3)
        self.assertIn("nastajanju", status)
        self.assertEqual(len(af.history()), 1)

    def test_sound_transition(self):
        agent = Agent("A")
        zvok = AgentZvok()
        status = zvok.receive_frequency(agent, 2.0)
        self.assertIn("Zven", status)
        self.assertEqual(agent.state, "Jaz")
        self.assertEqual(len(zvok.history()), 1)


if __name__ == "__main__":
    unittest.main()
