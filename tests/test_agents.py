import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.set_emotion("strah", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_on_tension(self):
        agent = Agent("B")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=2)
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
