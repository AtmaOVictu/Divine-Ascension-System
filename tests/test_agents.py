import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_response(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion("joy", 0.4)
        self.assertIn("Veseli", agent.respond())

    def test_dialogue_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertIn(a2.state, ("Jaz", "Enotnost"))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("eno" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
