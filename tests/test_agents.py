import unittest
from divine_agents.agent import Agent, team_decision
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
        agent = Agent("A", loyalty=0.8, emotion=0.2)
        decision = agent.make_moral_decision("test")
        self.assertIn("helps others", decision)

    def test_team_decision(self):
        team = [Agent("A", emotion=0.9), Agent("B", emotion=0.8)]
        choice = team_decision(team)
        self.assertIn("risk", choice)


if __name__ == '__main__':
    unittest.main()
