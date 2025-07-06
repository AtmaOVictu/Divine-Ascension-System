import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.enlightenment import Mediator, Meditation, Transformacija


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

    def test_mediation(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        mediator = Mediator("M")
        msg = mediator.mediate(a1, a2)
        self.assertIn("Jaz", msg)
        self.assertEqual(a1.state, "Jaz")

    def test_meditation(self):
        a1 = Agent("A1")
        meditation = Meditation(a1)
        note = meditation.meditate()
        self.assertIn("Jaz", note)
        self.assertEqual(a1.state, "Jaz")

    def test_transformacija(self):
        a1 = Agent("A1", state="Jaz")
        trans = Transformacija(a1)
        note = trans.transform()
        self.assertIn("Enotnost", note)
        self.assertEqual(a1.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
