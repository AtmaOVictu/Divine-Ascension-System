import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents import Agent, Cluster


class TestCluster(unittest.TestCase):
    def test_cluster_runs(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        cluster = Cluster([a1, a2])
        transcript = cluster.run(rounds=1)
        # after one run, both agents should have transitioned once
        self.assertEqual(a1.history[-1], "Jaz")
        self.assertEqual(a2.history[-1], "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in transcript))


if __name__ == "__main__":
    unittest.main()
