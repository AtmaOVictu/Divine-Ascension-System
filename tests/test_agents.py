import unittest
from divine_agents.agent import (
    Agent,
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue


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


class TestExtendedAgents(unittest.TestCase):
    def test_reason_agent(self):
        agent = ReasonAgent("R")
        agent.update_logic(0.6)
        self.assertIn("valid interpretation", agent.reason("test"))
        agent.update_tension(0.9)
        self.assertEqual(agent.transition(), "Jaz")

    def test_interpolation_agent(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        interp = InterpolationAgent("I", interpolation_level=0.6)
        self.assertIn("connection is possible", interp.interpolate(a1, a2))

    def test_intercontinentalization_agent(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        inter = IntercontinentalizationAgent("IC", reach=0.6)
        self.assertIn("dimensional boundaries", inter.connect_worlds(a1, a2))

    def test_emotional_dialogue(self):
        a1 = Agent("AA")
        a2 = Agent("BB")
        lines = emotional_dialogue(a1, a2)
        self.assertTrue(any("odziv" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
