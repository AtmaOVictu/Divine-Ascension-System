import unittest
from divine_agents.agent import Agent, GradualAgent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_emotion_trigger(self):
        agent = GradualAgent("Test")
        agent.update_emotion("anger", 0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_gradual_transition(self):
        agent = GradualAgent("Test")
        agent.update_emotion("joy", 0.3)
        self.assertEqual(agent.state, "Jaz")
        agent.update_emotion("anger", 0.5)
        self.assertEqual(agent.state, "Enotnost")

    def test_dialogue_emotions(self):
        a1 = GradualAgent("A1")
        a2 = GradualAgent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
