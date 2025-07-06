import unittest
from divine_agents.agent import Agent
from divine_agents.sensors import AgentFrekvenca, AgentZvok


class TestSensors(unittest.TestCase):
    def test_frequency_status(self):
        det = AgentFrekvenca()
        status = det.detect("Ego", 0.3)
        self.assertIn("Nizka", status)
        self.assertEqual(len(det.history()), 1)

    def test_zvok_causes_transition(self):
        det = AgentFrekvenca()
        zvok = AgentZvok(det)
        agent = Agent("A")
        zvok.resonate(agent, 2.0)
        self.assertEqual(agent.state, "Jaz")
        self.assertEqual(len(det.history()), 1)


if __name__ == '__main__':
    unittest.main()
