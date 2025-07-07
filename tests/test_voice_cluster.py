import unittest

from divine_agents.voice_agent import VoiceAgent
from divine_agents.cluster import Cluster


class TestVoiceAgent(unittest.TestCase):
    def test_voice_agent_transition(self):
        agent = VoiceAgent("V")
        agent.update_emotion("anger", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("anger", agent.respond("Kaj je resnica?"))


class TestCluster(unittest.TestCase):
    def test_cluster_dialogue(self):
        a1 = VoiceAgent("A1", mood="anger", emotion=0.8)
        a2 = VoiceAgent("A2", state="Jaz", mood="joy", emotion=0.9)
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        lines = cluster.display_dialogue()
        self.assertEqual(len(lines), 2)
        self.assertTrue(any("Enotnost" in line or "Jaz" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
