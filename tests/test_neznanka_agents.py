import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.neznanka_agents import (
    AgentNEZNANKA,
    AgentNEZNANKA_ZVOK,
    AgentPI,
    AgentROM,
)


class TestNeznankaAgents(unittest.TestCase):
    def test_neznanka_status(self):
        agent = AgentNEZNANKA()
        _, status = agent.zaznaj("priloznost za akcijo")
        self.assertEqual(status, "priloznost")

    def test_neznanka_zvok(self):
        agent = AgentNEZNANKA_ZVOK()
        result = agent.zaznaj_in_zveni("neizrecen potencial")
        self.assertIn("zven", result)

    def test_agent_pi(self):
        agent = AgentPI()
        _, status = agent.zaznaj("presledek kot zacetek")
        self.assertEqual(status, "rast")

    def test_agent_rom(self):
        agent = AgentROM()
        _, status = agent.rast("alarm zaznan kot odgovor")
        self.assertEqual(status, "prehod")


if __name__ == '__main__':
    unittest.main()
