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

    def test_history_only_on_change(self):
        agent = Agent("A")
        agent.update_tension(0.5)
        agent.transition()
        self.assertEqual(len(agent.history), 1)

    def test_calm_down(self):
        agent = Agent("A")
        agent.update_emotion(0.4)
        agent.calm_down(0.2)
        self.assertLess(agent.emotion, 0.4)
        self.assertLess(agent.tension, 0.4)


if __name__ == '__main__':
    unittest.main()
