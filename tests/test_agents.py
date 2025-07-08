import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, decision_process


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

    def test_fame_update(self):
        agent = Agent("F")
        fame = agent.update_fame(positive_actions=3, negative_actions=1, participation_score=50)
        self.assertGreater(fame, 0)

    def test_decision_process(self):
        a1 = Agent("A1", fame=20, participation=40)
        a2 = Agent("A2", fame=10, participation=60)
        influences = decision_process([a1, a2])
        self.assertEqual(len(influences), 2)
        self.assertAlmostEqual(sum(influences), 100.0, delta=0.0001)


if __name__ == '__main__':
    unittest.main()
