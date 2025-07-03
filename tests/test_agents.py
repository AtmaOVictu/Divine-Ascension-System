import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotion_driven_dialogue
from divine_agents.emotion_utils import emotion_cycle


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


class TestEmotionCycle(unittest.TestCase):
    def test_cycle_basic(self):
        self.assertAlmostEqual(emotion_cycle(0), 0.0)
        self.assertAlmostEqual(emotion_cycle(0.25, frequency=1), 1.0, places=5)


class TestEmotionDrivenDialogue(unittest.TestCase):
    def test_emotion_driven_dialogue_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotion_driven_dialogue(a1, a2, steps=10)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
