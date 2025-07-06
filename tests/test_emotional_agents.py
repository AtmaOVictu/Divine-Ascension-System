import unittest
from divine_agents.emotional import EmotionalAgent, EmotionState, emotional_dialogue

class TestEmotionalAgent(unittest.TestCase):
    def test_emotional_transition(self):
        agent = EmotionalAgent("B")
        agent.set_emotion("fear", 0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_dialogue_contains_states(self):
        a1 = EmotionalAgent("A1")
        a2 = EmotionalAgent("A2", state="Jaz")
        convo = emotional_dialogue(a1, a2)
        joined = "\n".join(convo)
        self.assertIn("absolutna", joined)
        self.assertIn("relativna", joined)

if __name__ == '__main__':
    unittest.main()
