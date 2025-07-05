import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, complex_dialogue
from divine_agents.shadows import UrgentShadow
from divine_agents.axis import SecondTrueAxis
from divine_agents.null_space import NullSpace


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

    def test_emotion_influence(self):
        agent = Agent("E")
        agent.apply_emotion("strah", 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)

    def test_urgent_shadow(self):
        agent = Agent("S")
        shadow = UrgentShadow("Temna", 0.9)
        shadow.trigger(agent)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_second_axis(self):
        axis = SecondTrueAxis("A", 0.6)
        self.assertEqual(axis.determine_direction(), "proactive")

    def test_null_space(self):
        space = NullSpace()
        space.stabilize()
        self.assertEqual(space.state, "stable")

    def test_complex_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        shadow = UrgentShadow("T", 0.9)
        axis = SecondTrueAxis("Ax", 0.7)
        lines = complex_dialogue(a1, a2, shadow, axis)
        self.assertTrue(any("smer" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
