import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.omnipotent import OmnipotentAgent


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
    def test_assign_and_feedback(self):
        a1 = Agent("A")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([a1])
        omni.analyze_agents()
        report = omni.provide_feedback()
        self.assertIn("A", report)

    def test_control_transition(self):
        a1 = Agent("A")
        a1.update_tension(0.8)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(a1)
        self.assertEqual(a1.state, "Enotnost")

if __name__ == "__main__":
    unittest.main()

