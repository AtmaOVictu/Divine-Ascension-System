import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.3)
        agent.update_emotion(0.3)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_jaz_to_enotnost_transition(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_dialogue_states_before_after(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("A1 (Ego)", lines[0])
        self.assertIn("A2 (Jaz)", lines[1])
        self.assertIn("A1 prehaja v stanje: Jaz", lines[2])
        self.assertIn("A2 prehaja v stanje: Enotnost", lines[3])
        self.assertIn("relativna", lines[4])
        self.assertIn("eno", lines[5])


if __name__ == '__main__':
    unittest.main()
