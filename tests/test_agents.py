import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, VoiceAgent, Cluster, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("What is truth?")
        self.assertIn("one", reply)

    def test_dialogue(self):
        a1 = VoiceAgent("A1", mood="anger")
        a2 = VoiceAgent("A2", state="Jaz", mood="joy")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("transitions to" in line for line in lines))

    def test_cluster_synchronize(self):
        a1 = VoiceAgent("Agent1", mood="fear")
        a2 = VoiceAgent("Agent2", mood="joy")
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        self.assertEqual(len(cluster.history), 2)


if __name__ == '__main__':
    unittest.main()
