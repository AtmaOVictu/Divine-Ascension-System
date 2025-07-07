import random
import unittest

from divine_agents.voice_agent import VoiceAgent
from divine_agents.cluster import Cluster


class TestVoiceAgent(unittest.TestCase):
    def test_voice_transition(self):
        agent = VoiceAgent("A", mood="anger")
        agent.update_emotion("anger", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_voice_response(self):
        agent = VoiceAgent("B", state="Jaz", mood="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("veseljem", reply)


class TestCluster(unittest.TestCase):
    def test_cluster_dialogue(self):
        random.seed(0)
        a1 = VoiceAgent("A1", mood="anger")
        a2 = VoiceAgent("A2", state="Jaz", mood="joy")
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        dialogue = cluster.display_dialogue()
        # After synchronization, agents should have transitioned
        self.assertIn("Jaz", cluster.history[0])
        self.assertIn("Enotnost", cluster.history[1])
        self.assertEqual(len(dialogue), 2)


if __name__ == "__main__":
    unittest.main()
