import unittest
from unittest.mock import patch

from divine_agents.voice_agent import VoiceAgent
from divine_agents.cluster import Cluster


class TestVoiceAgent(unittest.TestCase):
    def test_emotion_based_transition(self):
        agent = VoiceAgent("A", mood="anger")
        agent.update_emotion("anger", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_response_tone(self):
        agent = VoiceAgent("B", state="Jaz", mood="joy")
        agent.update_emotion("joy", 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("spoken with joy", reply)


class TestCluster(unittest.TestCase):
    def test_cluster_synchronize(self):
        a1 = VoiceAgent("A1", mood="anger")
        a2 = VoiceAgent("A2", state="Jaz", mood="joy")
        cluster = Cluster([a1, a2])
        with patch('random.uniform', return_value=0.8):
            cluster.synchronize()
        self.assertEqual(a1.state, "Jaz")
        # emotion threshold triggers second agent's transition to Enotnost
        self.assertEqual(a2.state, "Enotnost")
        self.assertEqual(len(cluster.history), 2)


if __name__ == "__main__":
    unittest.main()
