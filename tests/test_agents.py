import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate
from divine_agents.states import State


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        transitioned = agent.transition_if_needed()
        self.assertTrue(transitioned)
        self.assertEqual(agent.state, State.JAZ)

    def test_transition_by_emotion(self):
        agent = Agent("B", state=State.JAZ)
        agent.update_emotion(0.6)
        transitioned = agent.transition_if_needed()
        self.assertTrue(transitioned)
        self.assertEqual(agent.state, State.ENOTNOST)

    def test_dialogue_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=State.JAZ)
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))
        # final lines should reflect current states
        self.assertIn(a1.state.value, lines[-2])
        self.assertIn(a2.state.value, lines[-1])


if __name__ == "__main__":
    unittest.main()
