import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, OntologicalState
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.JAZ.value)
        self.assertTrue(any("state" in bytes.fromhex(h).decode() for h in agent.potential_changes))

    def test_responses(self):
        agent = Agent("A", state=OntologicalState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        agent.update_emotion(0.9)
        self.assertTrue(agent.respond("?").endswith("!"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologicalState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
