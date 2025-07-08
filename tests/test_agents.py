import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.influence import decision_process


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

    def test_fame_calculation(self):
        agent = Agent("A")
        fame = agent.update_fame(2, 1, 50)
        self.assertEqual(fame, 115)

    def test_decision_process(self):
        a1 = Agent("A1", fame=100, participation=50)
        a2 = Agent("A2", fame=50, participation=50)
        influences = decision_process([a1, a2])
        self.assertAlmostEqual(sum(influences.values()), 100.0, places=2)


if __name__ == '__main__':
    unittest.main()
