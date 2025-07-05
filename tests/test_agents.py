import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        ego_agent = Agent("A", state="Ego")
        self.assertIn("absolutna", ego_agent.respond("Kaj je resnica?"))

        jaz_agent = Agent("B", state="Jaz")
        self.assertIn("relativna", jaz_agent.respond("Kaj je resnica?"))

        enotnost_agent = Agent("C", state="Enotnost")
        self.assertIn("eno", enotnost_agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotion types are recorded in the dialogue output
        self.assertTrue(any("\u2694" in line for line in lines))
        self.assertTrue(any("\u2665" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
