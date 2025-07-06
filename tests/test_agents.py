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
        agent = Agent("B", emotional_state="happy", loyalty=0.9)
        agent.make_moral_decision("a risky situation")
        self.assertIn("help others", agent.decisions_history[-1])

    def test_group_decision(self):
        agent1 = Agent("A", emotional_state="happy", loyalty=0.8)
        agent2 = Agent("B", emotional_state="fearful", loyalty=0.6)
        agent1.team = [agent1, agent2]
        agent1.team_decision()
        self.assertIn("avoids risk", agent2.decisions_history[-1])


if __name__ == '__main__':
    unittest.main()
