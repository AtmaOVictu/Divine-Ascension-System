import unittest
from divine_agents import Agent, VoiceAgent, Cluster, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_voice_agent_tone_and_transition(self):
        va = VoiceAgent("VA", mood="anger")
        va.update_emotion("anger", 0.8)
        self.assertIn("anger", va.respond("Kaj je resnica?"))
        state = va.transition()
        self.assertEqual(state, "Jaz")

    def test_cluster_synchronize(self):
        a1 = VoiceAgent("C1", mood="fear")
        a2 = VoiceAgent("C2", mood="joy")
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        self.assertEqual(len(cluster.history), 2)
        dialogue = cluster.display_dialogue()
        self.assertEqual(len(dialogue), 2)


if __name__ == '__main__':
    unittest.main()

