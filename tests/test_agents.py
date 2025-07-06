import unittest
from divine_agents.agent import Agent, OntologyState
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntologyState.JAZ)

    def test_responses(self):
        agent = Agent("A", state=OntologyState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologyState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any(OntologyState.ENOTNOST.value in line for line in lines))


if __name__ == '__main__':
    unittest.main()
