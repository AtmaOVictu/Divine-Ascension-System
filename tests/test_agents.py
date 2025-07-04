import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.insights import SpeedInsights


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

    def test_opposite_state(self):
        agent = Agent("A")
        opposite = agent.activate_opposite_state()
        self.assertEqual(opposite, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines, insights = philosophical_dialogue(a1, a2)
        self.assertTrue(any("nasprotno stanje" in line for line in lines))
        self.assertGreaterEqual(len(insights.get_events()), 1)


if __name__ == '__main__':
    unittest.main()
