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

    def test_history_records(self):
        agent = Agent("H")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_moral_decision_record(self):
        agent = Agent("M", loyalty=0.9)
        agent.update_emotion(0.6, "joy")
        decision = agent.make_moral_decision("test")
        self.assertIn("help others", decision)
        self.assertEqual(agent.decisions_history[-1], decision)

    def test_team_decision(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        team = [a1, a2]
        a1.team = team
        a2.team = team
        a1.update_tension(0.6)
        a2.update_tension(0.6)
        decision = a1.team_decision()
        self.assertEqual(decision, "avoids risk")
        self.assertIn("avoids risk", a1.decisions_history[-1])


if __name__ == '__main__':
    unittest.main()
