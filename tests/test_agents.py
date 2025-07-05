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

    def test_omnipotent_control(self):
        omni = OmnipotentAgent("Omni")
        agent = Agent("A")
        agent.update_tension(0.9)
        omni.control_transition(agent)
        self.assertEqual(agent.state, "Enotnost")

    def test_omnipotent_supervision(self):
        omni = OmnipotentAgent("Supervisor")
        a1 = Agent("A1")
        omni.assign_supervision([a1])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("A1", feedback)


if __name__ == '__main__':
    unittest.main()
