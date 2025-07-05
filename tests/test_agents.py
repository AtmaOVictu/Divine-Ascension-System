import unittest
from divine_agents import Agent, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.9, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("S strahom", agent.respond("Kaj je resnica?"))

        agent.update_emotion(0.9, "veselje")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")
        self.assertIn("Z veseljem", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect emotional prefixes and potential transition to Enotnost
        self.assertTrue(any("Z veseljem" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
