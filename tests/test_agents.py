import unittest
from divine_agents.agent import Agent, OntologicalState
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.JAZ.value)

        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, OntologicalState.ENOTNOST.value)

    def test_responses(self):
        agent = Agent("A", state=OntologicalState.ENOTNOST)
        agent.update_emotion(0.4, "joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("interconnected", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologicalState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Emotion" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
