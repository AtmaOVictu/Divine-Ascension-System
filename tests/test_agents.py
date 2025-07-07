import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.calibration import calibrate_tensions


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

    def test_calibration(self):
        a1 = Agent("A1", tension=0.3)
        a2 = Agent("A2", tension=0.4)
        calibrate_tensions([a1, a2], 2)
        self.assertAlmostEqual(a1.tension, 0.6)
        self.assertAlmostEqual(a2.tension, 0.8)
        # ensure state unchanged before transition
        self.assertEqual(a1.state, "Ego")
        self.assertEqual(a2.state, "Ego")
        a1.transition()
        a2.transition()
        self.assertEqual(a1.state, "Ego")
        self.assertEqual(a2.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
