import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.voice_agent import VoiceAgent
from divine_agents.cluster import Cluster


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


class TestVoiceAgentEmotions(unittest.TestCase):
    def test_individual_emotion_transition(self):
        angry = VoiceAgent("Angry", mood="anger")
        angry.update_emotion("anger", 0.8)
        state_angry = angry.transition()
        self.assertEqual(state_angry, "Jaz")

        joyful = VoiceAgent("Joy", mood="joy")
        joyful.update_emotion("joy", 0.3)
        state_joy = joyful.transition()
        self.assertEqual(state_joy, "Ego")

    def test_cluster_transition(self):
        a1 = VoiceAgent("A1", mood="anger")
        a2 = VoiceAgent("A2", mood="joy")
        cluster = Cluster([a1, a2])
        cluster.synchronize()
        dialogue = cluster.display_dialogue()
        self.assertEqual(len(dialogue), 4)
        self.assertTrue(any(agent.state in ("Jaz", "Enotnost") for agent in cluster.agents))


if __name__ == "__main__":
    unittest.main()
