import unittest
from divine_agents import Agent, MetaAgent, FilozofskiPrehod


class TestMetaAgent(unittest.TestCase):
    def test_analyze_transition_logs_message(self):
        agent = Agent("B")
        agent.update_tension(0.8)
        meta = MetaAgent(agent)
        msg = meta.analyze_transition()
        self.assertIn("Metaparadoks", msg)
        self.assertEqual(agent.state, "Jaz")

    def test_filozofski_prehod(self):
        agent = Agent("C", state="Jaz")
        fp = FilozofskiPrehod(agent)
        self.assertEqual(fp.prehod_resnice(), "Relativna resnica")


if __name__ == "__main__":
    unittest.main()

