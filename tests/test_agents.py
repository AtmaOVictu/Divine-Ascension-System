import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_thresholds(self):
        agent = Agent("B")
        agent.update_emotion(0.5)
        agent.update_tension(0.7)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertEqual(agent.history, ["Ego", "Ego"])

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_after_transitions(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_dialogue_state_responses(self):
        a1 = Agent("D1")
        a2 = Agent("D2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("absolutna", lines[0])
        self.assertIn("(Ego)", lines[0])
        self.assertIn("relativna", lines[1])
        self.assertIn("(Jaz)", lines[1])
        self.assertIn("relativna", lines[-2])
        self.assertIn("eno", lines[-1])


if __name__ == '__main__':
    unittest.main()
