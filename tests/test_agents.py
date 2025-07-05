import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.omnipotent_agent import OmnipotentAgent


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


class TestOmnipotentAgent(unittest.TestCase):
    def test_control_transition(self):
        agent = Agent("B")
        agent.update_tension(0.9)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(agent)
        self.assertEqual(agent.state, "Enotnost")

    def test_analysis_feedback(self):
        agent = Agent("C")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([agent])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("Agent C", feedback)


if __name__ == '__main__':
    unittest.main()
