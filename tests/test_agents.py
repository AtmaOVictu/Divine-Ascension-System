import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_high_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_jaz_to_enotnost_via_emotion(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion(0.7)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

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
        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])
        self.assertIn("Jaz", lines[2])
        self.assertIn("Enotnost", lines[3])
        self.assertIn("relativna", lines[4])
        self.assertIn("eno", lines[5])


if __name__ == '__main__':
    unittest.main()
