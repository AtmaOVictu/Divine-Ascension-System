import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # below threshold, state should remain the same
        agent.update_tension(0.6)
        self.assertEqual(agent.transition(), "Ego")

        # exceeding tension threshold triggers transition
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        # emotion threshold should trigger next transition
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        ego = Agent("EgoAgent", state="Ego")
        jaz = Agent("JazAgent", state="Jaz")
        eno = Agent("EnoAgent", state="Enotnost")

        self.assertIn("absolutna", ego.respond("Kaj je resnica?"))
        self.assertIn("relativna", jaz.respond("Kaj je resnica?"))
        self.assertIn("eno", eno.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)

        # after dialogue each agent should have transitioned once
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)

        # verify lines reflect states after transition
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_invalid_state(self):
        with self.assertRaises(ValueError):
            Agent("Bad", state="Unknown")


if __name__ == '__main__':
    unittest.main()
