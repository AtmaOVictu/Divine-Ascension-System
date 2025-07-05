import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.omnipotent_agent import OmnipotentAgent
from divine_agents.agent import Agent


class TestOmnipotentAgent(unittest.TestCase):
    def test_supervision_and_feedback(self):
        a1 = Agent("A1")
        a1.update_emotion(-0.6)
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([a1])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("negative emotions", feedback)

    def test_control_transition(self):
        a1 = Agent("A1", tension=0.8)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(a1)
        self.assertEqual(a1.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
