import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.multilingual_agent import MultilingualAgent
from divine_agents.dialogue import multilingual_dialogue


class TestMultilingualAgent(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = MultilingualAgent("A", language="Spanish")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_language(self):
        agent = MultilingualAgent("B", language="German", state="Enotnost")
        reply = agent.respond("What is truth?")
        self.assertIn("Wahrheit", reply)

    def test_dialogue_progression(self):
        a1 = MultilingualAgent("A1", language="English")
        a2 = MultilingualAgent("A2", language="French", state="Jaz")
        a1.update_tension(0.8)
        a2.update_tension(0.8)
        lines = multilingual_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line or "interconnect" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
