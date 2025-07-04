import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.phase, 2)

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion=0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("čustva", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("faza" in line for line in lines))

    def test_permutation(self):
        agent = Agent("B", phase=10)
        agent.permute()
        self.assertGreater(agent.phase, 10)

    def test_degradation(self):
        agent = Agent("C", phase=5)
        agent.update_tension(0.1)
        agent.transition()
        self.assertLess(agent.phase, 5)


if __name__ == '__main__':
    unittest.main()
