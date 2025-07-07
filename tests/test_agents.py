import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue
from divine_agents.emotions import EmotionalBox, EmotionalAgent


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

    def test_emotional_box(self):
        box = EmotionalBox("anger")
        status = box.process(EmotionalAgent())
        self.assertEqual(status, "Emotion confirmed: Negative")

    def test_emotional_dialogue_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2, "anger", "joy")
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
