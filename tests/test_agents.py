import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, PhilosophicalDebate
from divine_agents.ontology import OntologicalLibrary


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


class TestOntology(unittest.TestCase):
    def test_opposite_lookup(self):
        lib = OntologicalLibrary()
        self.assertEqual(lib.get_opposite("Veselje"), "Trpljenje")

    def test_debate_transitions(self):
        lib = OntologicalLibrary()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        debate = PhilosophicalDebate(a1, a2, lib)
        lines = debate.run()
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Prehod" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
