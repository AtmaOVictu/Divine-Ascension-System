import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import Agent, AgentCluster


class TestAgentCluster(unittest.TestCase):
    def test_cluster_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        cluster = AgentCluster()
        cluster.add_agent(a1)
        cluster.add_agent(a2)

        a1.update_emotion(0.8)
        a2.update_tension(0.9)

        cluster.transition_agents()

        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")
        cluster.synchronize_emotions()
        self.assertAlmostEqual(a1.emotion, a2.emotion)

    def test_cluster_state(self):
        a1 = Agent("A1", state="Enotnost")
        a2 = Agent("A2", state="Enotnost")
        cluster = AgentCluster([a1, a2])
        cluster.update_cluster_state()
        self.assertEqual(cluster.cluster_state, "Unified")


if __name__ == "__main__":
    unittest.main()
