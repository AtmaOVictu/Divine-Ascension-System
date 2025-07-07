import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.membership import MembershipAgent, InterpretiveAgent


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

    def test_membership_join(self):
        m1 = MembershipAgent("M1")
        m2 = MembershipAgent("M2")
        m1.update_emotion(0.9)
        joined = m1.ionize_environment(m2)
        self.assertTrue(joined)
        self.assertEqual(m1.group, "M2")

    def test_interpret_change(self):
        base = Agent("B", state="Enotnost")
        interp = InterpretiveAgent("I")
        interp.interpret_change(base)
        self.assertEqual(interp.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()

