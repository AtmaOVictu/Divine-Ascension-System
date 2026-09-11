import unittest
from divine_agents import Agent, OntologyState, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, OntologyState.JAZ)
        self.assertIn("High Tension Box", agent.new_boxes)

    def test_responses(self):
        agent = Agent("A", state=OntologyState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_clamping(self):
        agent = Agent("A")
        agent.update_emotion(1.5)
        self.assertLessEqual(agent.emotion, 1.0)

    def test_multi_transition_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntologyState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))



if __name__ == '__main__':
    unittest.main()
