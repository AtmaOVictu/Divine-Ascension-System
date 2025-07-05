import unittest

from divine_agents.agent import Agent, Emotions, State, Debate
from divine_agents.dialogue import philosophical_dialogue


class AgentSystemTest(unittest.TestCase):
    """Unit tests for the ontological agent system."""

    def test_transition_ego_to_jaz(self):
        agent = Agent("A", state=State.EGO, tension=0.8)
        agent.update_state()
        self.assertEqual(agent.state, State.JAZ)

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state=State.JAZ, tension=0.8)
        agent.update_state()
        self.assertEqual(agent.state, State.ENOTNOST)

    def test_emotion_triggered_transition(self):
        agent = Agent("C")
        agent.feel(fear=0.6)
        agent.update_state()
        self.assertEqual(agent.state, State.JAZ)

    def test_dialogue_responses(self):
        a = Agent("A", state=State.EGO)
        b = Agent("B", state=State.JAZ)
        debate = Debate(a, b)
        resp_a, resp_b = debate.step()
        self.assertIn("absolute", resp_a)
        self.assertIn("relative", resp_b)

    def test_philosophical_dialogue(self):
        a = Agent("A")
        b = Agent("B", state=State.JAZ)
        lines = philosophical_dialogue(a, b)
        self.assertTrue(any("interconnected" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

