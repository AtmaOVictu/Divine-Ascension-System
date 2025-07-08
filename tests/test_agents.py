import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.philosophy import State, PHILOSOPHICAL_TRUTHS


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, State.JAZ)

    def test_emotion_threshold(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, State.JAZ)

    def test_responses(self):
        agent = Agent("A", state=State.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertEqual(reply, PHILOSOPHICAL_TRUTHS[State.ENOTNOST])

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=State.JAZ)
        lines = philosophical_dialogue(a1, a2)
        # At least one line should mention Enotnost after transition
        self.assertTrue(any(State.ENOTNOST.value in line for line in lines))


if __name__ == '__main__':
    unittest.main()
