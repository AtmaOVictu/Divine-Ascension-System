import unittest
from divine_agents import Agent, OmnipotentAgent


class TestOmnipotentAgent(unittest.TestCase):
    def test_assign_and_analyze(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([a1, a2])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("Assigned supervision", feedback)
        self.assertIn("Agent A1", feedback)

    def test_control_transition(self):
        target = Agent("Target")
        target.update_tension(0.8)
        omni = OmnipotentAgent("Controller")
        omni.control_transition(target)
        self.assertEqual(target.state, "Enotnost")
        self.assertIn("Controller", target.history[-1])


if __name__ == "__main__":
    unittest.main()

