import unittest
from divine_agents import Agent, OntologyState, philosophical_dialogue


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
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_clamping_and_box_creation(self):
        agent = Agent("B")
        agent.update_emotion(1.2)
        self.assertEqual(agent.emotion, 1.0)
        self.assertTrue(any(box.name == "Extreme Emotion Box" for box in agent.new_boxes))

    def test_sequential_transitions(self):
        agent = Agent("C")
        agent.update_emotion(0.9)
        agent.transition()
        self.assertEqual(agent.state, OntologyState.JAZ)
        agent.update_emotion(0.9)
        agent.transition()
        self.assertEqual(agent.state, OntologyState.ENOTNOST)


if __name__ == '__main__':
    unittest.main()
