import unittest

from divine_agents import Agent, philosophical_dialogue, Emotion, AgentNetwork, Karma


class TestInteractions(unittest.TestCase):
    def test_network_emotion_update(self):
        net = AgentNetwork(2)
        net.update_emotions([[0, 1], [1, 0]])
        self.assertEqual(net.emotions, [0.0, 0.0])

    def test_karma_update(self):
        karma = Karma()
        emotion = Emotion(joy=0.9)
        result = karma.update(emotion, 0.0)
        self.assertGreater(result, 0)

    def test_dialogue_contains_states(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Ego" in line or "Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
