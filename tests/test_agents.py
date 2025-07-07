import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("A")
        self.assertIn("absolutna", ego.respond("Kaj je resnica?"))

        jaz = Agent("B", state="Jaz")
        self.assertIn("relativna", jaz.respond("Kaj je resnica?"))

        enotnost = Agent("C", state="Enotnost")
        self.assertIn("eno", enotnost.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("jeza" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
