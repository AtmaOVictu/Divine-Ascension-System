import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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
        self.assertTrue(any("RES" in line for line in lines))

    def test_phase_evolution(self):
        agent = Agent("P")
        start = agent.phase
        agent.evolve()
        self.assertEqual(agent.phase, start + 1)

    def test_phase_degradation(self):
        agent = Agent("P", phase=5)
        agent.degrade()
        self.assertEqual(agent.phase, 4)

    def test_phase_permutation(self):
        agent = Agent("P", phase=50)
        new_phase = agent.permute()
        self.assertTrue(1 <= new_phase <= 100)


if __name__ == '__main__':
    unittest.main()
