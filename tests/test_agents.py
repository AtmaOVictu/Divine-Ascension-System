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
        self.assertEqual(a1.state, "Jaz")
        self.assertIn(a2.state, ["Jaz", "Enotnost"])

    def test_influence(self):
        a1 = Agent("A1", tension=0.1, emotion=0.5)
        a2 = Agent("A2", tension=0.1, emotion=0.0)
        a1.influence(a2)
        self.assertGreater(a2.emotion, 0.0)


if __name__ == '__main__':
    unittest.main()
