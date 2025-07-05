import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

class TestAdditionalTransitions(unittest.TestCase):
    def test_emotion_threshold_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_two_step_transition_to_enotnost(self):
        agent = Agent("B")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_dialogue_state_changes(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("A1 prehaja v stanje: Jaz", lines)
        self.assertIn("A2 prehaja v stanje: Enotnost", lines)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

if __name__ == '__main__':
    unittest.main()
