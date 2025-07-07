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
        lines = philosophical_dialogue(a1, a2, turns=3)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn("A1", lines[0])
        self.assertGreaterEqual(len(lines), 6)

    def test_express_truth(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        text = agent.express_truth()
        self.assertIn("strastno", text)


if __name__ == '__main__':
    unittest.main()
