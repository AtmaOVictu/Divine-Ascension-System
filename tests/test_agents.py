import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_moral_decision(self):
        agent = Agent("B", loyalty=0.8, emotion=0.6)
        decision = agent.make_moral_decision("preizkus")
        self.assertIn("selflessly", decision)

    def test_team_decision(self):
        leader = Agent("Leader")
        m1 = Agent("M1")
        m2 = Agent("M2")
        leader.update_relationship(m1, 0.3)
        leader.update_relationship(m2, 0.3)
        result = leader.team_decision([m1, m2])
        self.assertIn("risk", result)


if __name__ == '__main__':
    unittest.main()
