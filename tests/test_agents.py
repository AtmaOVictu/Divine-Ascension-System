import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.loading import LoadingScreenUnity


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

    def test_emotion_transition(self):
        agent = Agent("A")
        agent.express_emotion("fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_loading_screen(self):
        loader = LoadingScreenUnity("L", min_value=0.0, max_value=0.02)
        loader.display()
        self.assertEqual(loader.unity_value, loader.min_value)
        self.assertAlmostEqual(loader.history[-1], 0.02, places=2)


if __name__ == '__main__':
    unittest.main()
