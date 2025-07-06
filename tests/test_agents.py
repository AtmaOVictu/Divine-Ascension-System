import unittest

from divine_agents import Agent, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("T")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("E", state="Jaz")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        a = Agent("A", state="Ego")
        self.assertIn("absolutna", a.respond("Kaj je resnica?"))
        a.state = "Jaz"
        self.assertIn("relativna", a.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure at least one agent reaches Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
