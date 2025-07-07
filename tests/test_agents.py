import unittest
from divine_agents import (
    Agent,
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
    philosophical_dialogue,
    extended_dialogue,
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

    def test_reason_agent(self):
        r = ReasonAgent("R", logic_level=0.6)
        self.assertIn("veljaven", r.reason("test"))

    def test_interpolation_agent(self):
        i = InterpolationAgent("I", interpolation_level=0.6)
        a1 = Agent("A1")
        a2 = Agent("A2")
        self.assertIn("možna je povezava", i.interpolate(a1, a2))

    def test_intercontinental_agent(self):
        ic = IntercontinentalizationAgent("IC", reach=0.6)
        a1 = Agent("A1")
        a2 = Agent("A2")
        self.assertIn("Povezujem", ic.connect_worlds(a1, a2))

    def test_extended_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        r = ReasonAgent("R", logic_level=0.7)
        interp = InterpolationAgent("Interp", interpolation_level=0.7)
        intercon = IntercontinentalizationAgent("Intercon", reach=0.8)
        lines = extended_dialogue(a1, a2, r, interp, intercon)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
