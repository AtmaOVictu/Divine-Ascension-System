import unittest

from divine_agents import Agent, AgentCluster


class TestAgentCluster(unittest.TestCase):
    def test_cluster_update_transitions(self):
        a1 = Agent("A1", tension=0.8)
        a2 = Agent("A2", state="Jaz", emotion=0.6)
        cluster = AgentCluster([a1, a2])
        states = cluster.update()
        self.assertEqual(states["A1"], "Jaz")
        self.assertEqual(states["A2"], "Enotnost")

    def test_check_states(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        cluster = AgentCluster([a1, a2])
        self.assertEqual(cluster.check_states(), {"A1": "Ego", "A2": "Jaz"})


if __name__ == "__main__":
    unittest.main()

