import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, debate_truth


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_truth(self):
        ego = Agent("E1")
        jaz = Agent("J1", state="Jaz")
        lines = debate_truth(ego, jaz)
        self.assertEqual(ego.state, "Jaz")
        self.assertEqual(jaz.state, "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
