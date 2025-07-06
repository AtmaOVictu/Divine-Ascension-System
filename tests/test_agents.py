import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, OntologicalState
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.JAZ)

    def test_responses(self):
        agent = Agent("A", state=OntologicalState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologicalState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_influence(self):
        agent = Agent("A")
        agent.update_emotion(0.9, "fear")
        self.assertGreater(agent.tension, 0.0)
        agent.transition()
        self.assertEqual(agent.state, OntologicalState.JAZ)


if __name__ == '__main__':
    unittest.main()
