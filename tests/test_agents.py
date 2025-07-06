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
        lines = philosophical_dialogue(a1, a2, rounds=3)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_influence_transition(self):
        a1 = Agent("A1", tension=0.6, emotion=0.4)
        a2 = Agent("A2", tension=0.9, emotion=0.9)
        a1.influence(a2)
        state = a1.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
