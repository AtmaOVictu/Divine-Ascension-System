import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import advanced_dialogue


class TestAdvancedDialogue(unittest.TestCase):
    def test_emotion_triggers_transition(self):
        agent = Agent('A')
        agent.update_emotion(0.6, 'fear')
        self.assertEqual(agent.transition(), 'Jaz')

    def test_dialogue_contains_emotions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        transcript = advanced_dialogue(a1, a2, rounds=1)
        joined = '\n'.join(transcript)
        self.assertIn('anger', joined)
        self.assertIn('joy', joined)


if __name__ == '__main__':
    unittest.main()
