import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        jaz = Agent("J", state="Jaz")
        enotnost = Agent("En", state="Enotnost")
        self.assertIn("absolutna", ego.respond("?"))
        self.assertIn("relativna", jaz.respond("?"))
        self.assertIn("eno", enotnost.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Dialogue should show transitions and philosophical statements
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
