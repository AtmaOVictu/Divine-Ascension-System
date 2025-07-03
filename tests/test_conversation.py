import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.conversation import emotional_debate


class TestConversation(unittest.TestCase):
    def test_state_transition_emotion(self):
        agent = Agent('A')
        agent.update_emotion(0.6, 'fear')
        self.assertEqual(agent.transition(), 'Jaz')
        self.assertEqual(agent.emotion_label, 'fear')

    def test_emotional_debate(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = emotional_debate(a1, a2)
        # Ensure transitions occurred
        self.assertTrue(any('Enotnost' in l for l in lines))
        # Ensure emotional labels appear in dialogue
        self.assertTrue(any('čuti' in l for l in lines))


if __name__ == '__main__':
    unittest.main()
