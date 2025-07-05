import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, advanced_philosophical_dialogue
from divine_agents.onto_agent import OntologicalAgent


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


class TestOntologicalAgent(unittest.TestCase):
    def test_parental_influence(self):
        birth = {"initial_tension": 0.2, "initial_emotion": 0.1}
        parent = {"parental_tension": 0.3, "parental_emotion": 0.2, "parental_pathos": 0.1}
        agent = OntologicalAgent("B", birth, parent)
        self.assertAlmostEqual(agent.tension, 0.5)
        self.assertAlmostEqual(agent.emotion, 0.3)
        self.assertAlmostEqual(agent.pathos, 0.1)

    def test_transition_with_pathos(self):
        birth = {}
        parent = {"parental_pathos": 6}
        agent = OntologicalAgent("B", birth, parent)
        agent.optimize_transition()
        self.assertEqual(agent.state, "Jaz")

    def test_advanced_dialogue(self):
        birth = {}
        parent = {}
        a1 = OntologicalAgent("A1", birth, parent)
        a2 = OntologicalAgent("A2", birth, parent, state="Jaz")
        lines = advanced_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
