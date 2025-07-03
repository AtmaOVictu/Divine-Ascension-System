import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.interpolation import interpolate_differences


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

    def test_interpolation(self):
        a1 = Agent("A1", emotion=0.6, tension=0.4)
        a2 = Agent("A2", emotion=0.2, tension=0.3)
        a1.update_emotion(0.9)
        a2.update_emotion(0.5)
        time, emo_interp, tens_interp = interpolate_differences(a1, a2, steps=5)
        self.assertEqual(len(time), 5)
        self.assertEqual(len(emo_interp), 5)
        self.assertEqual(len(tens_interp), 5)


if __name__ == '__main__':
    unittest.main()
