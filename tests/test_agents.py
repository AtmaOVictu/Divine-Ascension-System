import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_thresholds_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        self.assertIn("absolutna", ego.respond("Kaj je resnica?"))
        jaz = Agent("J", state="Jaz")
        self.assertIn("relativna", jaz.respond("Kaj je resnica?"))
        eno = Agent("N", state="Enotnost")
        self.assertIn("eno", eno.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("anger" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
