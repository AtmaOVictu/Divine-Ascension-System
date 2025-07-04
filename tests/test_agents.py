import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.cycles import continuous_cycle


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

    def test_continuous_cycle(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = continuous_cycle(a1, a2, iterations=3)
        self.assertEqual(len(a1.history), 4)
        self.assertEqual(len(a2.history), 4)
        self.assertEqual(len(lines), 15)


if __name__ == '__main__':
    unittest.main()
