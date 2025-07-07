import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")
        agent.update_emotion(0.6, "joy")
        self.assertEqual(agent.transition(), "Enotnost")

    def test_emotion_based_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Vse resnice", reply)
        agent.update_emotion(0.6, "anger")
        self.assertIn("jezo", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Check that both agents transitioned at least once
        self.assertTrue(any("A1 prehaja" in line for line in lines))
        self.assertTrue(any("A2 prehaja" in line for line in lines))



if __name__ == '__main__':
    unittest.main()
