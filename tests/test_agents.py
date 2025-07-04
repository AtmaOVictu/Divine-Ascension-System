import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.res_phases import create_res_phases


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

    def test_res_phase_generation(self):
        phases = create_res_phases()
        self.assertEqual(len(phases), 103)
        self.assertEqual(phases[0].label, "RES0")
        self.assertEqual(phases[1].label, "RES00")
        self.assertEqual(phases[2].label, "RES000")
        self.assertEqual(phases[-1].label, "RES100")


if __name__ == '__main__':
    unittest.main()
