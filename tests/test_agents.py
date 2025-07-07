import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_debate_transitions(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=3)
        self.assertIn("Enotnost", a1.state)
        self.assertIn("Enotnost", a2.state)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))

    def test_debate_initial_responses(self):
        a1 = Agent("Start1")
        a2 = Agent("Start2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=1)
        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])


if __name__ == '__main__':
    unittest.main()
