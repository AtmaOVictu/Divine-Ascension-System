import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        jaz = Agent("J", state="Jaz")
        eno = Agent("N", state="Enotnost")
        self.assertIn("absolutna", ego.respond("Kaj je resnica?"))
        self.assertIn("relativna", jaz.respond("Kaj je resnica?"))
        self.assertIn("eno", eno.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect references to all truth perspectives
        combined = "\n".join(lines)
        self.assertIn("absolutna", combined)
        self.assertIn("relativna", combined)
        self.assertIn("eno", combined)


if __name__ == '__main__':
    unittest.main()
