import unittest
from divine_agents import (
    Agent,
    ContextualAgent,
    philosophical_dialogue,
    contextual_dialogue,
)


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

    def test_contextual_transition(self):
        ca1 = ContextualAgent("C1")
        ca2 = ContextualAgent("C2")
        ca1.set_context("visoka napetost", "stresno okolje")
        ca2.set_context("mirno", "podpora")
        ca1.contextual_transition()
        ca2.contextual_transition()  # first transition to Jaz
        ca2.contextual_transition()  # second transition to Enotnost
        self.assertEqual(ca1.state, "Jaz")
        self.assertEqual(ca2.state, "Enotnost")

    def test_contextual_dialogue(self):
        ca1 = ContextualAgent("A1")
        ca2 = ContextualAgent("A2")
        ca1.set_context("visoka napetost", "stresno okolje")
        ca2.set_context("mirno", "podpora")
        lines = contextual_dialogue(ca1, ca2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
