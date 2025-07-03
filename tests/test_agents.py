import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure at least one agent reaches Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_responses(self):
        ego = Agent("E")
        jaz = Agent("J", state="Jaz")
        enotnost = Agent("N", state="Enotnost")
        self.assertIn("absolutna", ego.respond("?"))
        self.assertIn("relativna", jaz.respond("?"))
        self.assertIn("eno", enotnost.respond("?"))


if __name__ == "__main__":
    unittest.main()
