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

    def test_omnipotent_feedback_and_control(self):
        ag1 = Agent("C1")
        ag2 = Agent("C2", state="Jaz")
        ag1.history.append("compete")
        ag2.history.append("cooperate")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([ag1, ag2])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("too competitive", feedback)
        self.assertIn("cooperative", feedback)

        ag1.update_tension(0.9)
        omni.control_transition(ag1)
        self.assertEqual(ag1.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
