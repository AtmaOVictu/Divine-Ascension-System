import unittest

from divine_agents.agent import Agent
from divine_agents.membership import MembershipAgent, InterpretiveAgent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_membership_transition(self):
        m1 = MembershipAgent("M1")
        m2 = MembershipAgent("M2", group="Group")
        m1.update_emotion(0.9)
        m1.transition(m2)
        self.assertEqual(m1.group, "Group")
        self.assertEqual(m1.state, "Jaz")

    def test_interpretive_agent(self):
        a = InterpretiveAgent("I1")
        other = MembershipAgent("M", state="Enotnost")
        a.interpret_change(other)
        self.assertEqual(a.state, "Enotnost")

    def test_dynamic_dialogue(self):
        a1 = MembershipAgent("A1")
        a2 = MembershipAgent("A2", group="G2")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any("state" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
