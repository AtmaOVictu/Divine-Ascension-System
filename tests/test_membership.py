import unittest
from divine_agents.membership import MembershipAgent, InterpretiveAgent
from divine_agents.debate import philosophical_debate


class TestMembershipAgents(unittest.TestCase):
    def test_ionization(self):
        a1 = MembershipAgent("A1")
        a2 = MembershipAgent("A2")
        a1.update_emotion(0.9)
        joined = a1.ionize_environment(a2)
        self.assertTrue(joined)
        self.assertEqual(a1.group, "A2")

    def test_interpret_change(self):
        interp = InterpretiveAgent("I1")
        other = InterpretiveAgent("I2", state="Enotnost")
        interp.interpret_change(other)
        self.assertEqual(interp.state, "Enotnost")

    def test_debate_transitions(self):
        a1 = MembershipAgent("A1")
        a2 = MembershipAgent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("prehaja" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
