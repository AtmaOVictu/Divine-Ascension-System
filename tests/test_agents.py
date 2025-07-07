import unittest

from divine_agents.agent import Agent, State
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, State.JAZ)

    def test_transition_by_emotion(self):
        agent = Agent("B", state=State.JAZ)
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, State.ENOTNOST)

    def test_responses(self):
        agent = Agent("A", state=State.ENOTNOST)
        reply = agent.respond("")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=State.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("čustveni naboj" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
