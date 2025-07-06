import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.metaparadox import MetaparadoxicalModule
from divine_agents.absolutes import RelativeAbsoluteLibrary


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

    def test_metaparadox(self):
        agent = Agent("B", emotion=0.6)
        module = MetaparadoxicalModule(agent)
        new_state = module.paradoxical_transition()
        self.assertEqual(new_state, "Jaz")

    def test_relative_absolute(self):
        lib = RelativeAbsoluteLibrary()
        truth = lib.get_absolute("truth")
        self.assertTrue(0.5 <= truth <= 1.5)


if __name__ == '__main__':
    unittest.main()
