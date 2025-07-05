import unittest
from divine_agents import Agent, OmnipotentAgent
from divine_agents.dialogue import philosophical_dialogue, emotive_dialogue


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
    def test_control_transition_to_enotnost(self):
        ag = Agent("T", tension=0.8)
        omni = OmnipotentAgent("O")
        omni.control_transition(ag)
        self.assertEqual(ag.state, "Enotnost")

    def test_analyze_agents(self):
        ag = Agent("T")
        ag.update_emotion(-0.6)
        omni = OmnipotentAgent("O")
        omni.assign_supervision([ag])
        omni.analyze_agents()
        self.assertIn("negative emotions", omni.provide_feedback())


class TestEmotiveDialogue(unittest.TestCase):
    def test_emotive_dialogue_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotive_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
