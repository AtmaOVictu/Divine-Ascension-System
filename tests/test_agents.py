import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.concept_library import (
    AbsoluteTruthLibrary,
    RelativeTruthLibrary,
    UnityOfGreedLibrary,
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


class TestConceptLibrary(unittest.TestCase):
    def test_absolute_library(self):
        lib = AbsoluteTruthLibrary()
        self.assertIn("absolutna", lib.get_truth())

    def test_relative_library(self):
        lib = RelativeTruthLibrary()
        self.assertIn("relativna", lib.get_truth())

    def test_unity_library(self):
        lib = UnityOfGreedLibrary()
        self.assertIn("eno", lib.get_truth())

    def test_agent_uses_library(self):
        agent = Agent("A", state="Jaz")
        response = agent.respond("Kaj je resnica?")
        self.assertEqual(response, RelativeTruthLibrary().get_truth())


if __name__ == '__main__':
    unittest.main()
