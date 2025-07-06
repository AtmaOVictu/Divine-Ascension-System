import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.agent import Agent, OntologicalState
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.JAZ)

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.JAZ)

    def test_responses(self):
        agent = Agent("C", state=OntologicalState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologicalState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        # At least one agent should reach ENOTNOST state
        self.assertTrue(any(OntologicalState.ENOTNOST.value in line for line in lines))


if __name__ == "__main__":
    unittest.main()
