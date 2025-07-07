import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_to_unity_and_reset(self):
        agent = Agent("B")
        agent.update_emotion("joy", 1.0)
        self.assertEqual(agent.history[-2], "Enotnost")
        self.assertEqual(agent.state, "Nujnost")
        self.assertEqual(agent.tension, 0.0)
        self.assertEqual(agent.emotion, 0.0)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Nujnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
