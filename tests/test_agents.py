import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import dialogue_round


class TestAgentTransitions(unittest.TestCase):
    def test_emotion_based_transitions(self):
        agent1 = Agent("Agent1", state="Ego", emotion="joy")
        agent2 = Agent("Agent2", state="Jaz", emotion="fear")

        agent1.transition()
        agent2.update_tension(0.8)
        agent2.transition()

        self.assertEqual(agent1.state, "Jaz")
        self.assertEqual(agent2.state, "Enotnost")
        self.assertIn("Emotion: joy", agent1.respond("Kaj je resnica?"))
        self.assertIn("Emotion: fear", agent2.respond("Kaj je resnica?"))

    def test_emotion_affects_response(self):
        agent1 = Agent("Agent1", state="Ego", emotion="joy")
        agent2 = Agent("Agent2", state="Jaz", emotion="anger")

        response1 = agent1.respond("Kaj je resnica?")
        response2 = agent2.respond("Kaj je resnica?")

        self.assertIn("Emotion: joy", response1)
        self.assertIn("Emotion: anger", response2)

    def test_dialogue_round(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dialogue_round(a1, a2, 2)
        self.assertTrue(len(lines) >= 4)
        self.assertTrue(any("Emotion:" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
