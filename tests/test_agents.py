import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        jaz = Agent("J", state="Jaz")
        eno = Agent("N", state="Enotnost")
        self.assertIn("absolutna", ego.respond("?"))
        self.assertIn("relativna", jaz.respond("?"))
        self.assertIn("eno", eno.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertIn(a2.state, ("Jaz", "Enotnost"))


if __name__ == '__main__':
    unittest.main()
