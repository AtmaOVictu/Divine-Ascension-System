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

    def test_fear_returns_to_axis(self):
        agent = Agent("Fearful", state="Jaz")
        agent.update_emotion(0.4, "fear")
        agent.transition()
        self.assertEqual(agent.state, agent.stable_axis)

    def test_history_records_transition(self):
        agent = Agent("Hist")
        agent.update_tension(0.9)
        agent.transition()
        self.assertTrue(any("transitional" in h for h in agent.history))


if __name__ == '__main__':
    unittest.main()
