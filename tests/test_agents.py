import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.75)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion("joy", 0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses_reflect_state(self):
        agent = Agent("C", state="Ego")
        self.assertIn("absolutna", agent.respond("Kaj?"))
        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("Kaj?"))
        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("Kaj?"))

    def test_dialogue_triggers_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("napetost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
