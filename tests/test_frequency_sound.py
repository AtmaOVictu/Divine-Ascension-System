import unittest
from divine_agents import Agent, AgentFrekvenca, AgentZvok


class TestFrekvencaZvok(unittest.TestCase):
    def test_frequency_detection(self):
        f = AgentFrekvenca()
        status = f.detect("Ego", 0.3)
        self.assertIn("Nizka frekvenca", status)

    def test_sound_transition(self):
        agent = Agent("A")
        zvok = AgentZvok(agent)
        zvok.process(2.0)
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()
