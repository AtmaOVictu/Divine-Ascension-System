import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import (
    Agent,
    philosophical_dialogue,
    Meditation,
    Mediator,
    Transformation,
)


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

    def test_meditation(self):
        agent = Agent("M")
        med = Meditation(agent)
        state = med.reflect()
        self.assertEqual(state, "Jaz")

    def test_mediation(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        mediator = Mediator("Med")
        state = mediator.mediate(a1, a2)
        self.assertEqual(state, "Jaz")

    def test_transformation(self):
        agent = Agent("T", state="Jaz")
        trans = Transformation(agent)
        state = trans.enforce()
        self.assertEqual(state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
