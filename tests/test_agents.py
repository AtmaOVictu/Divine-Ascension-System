import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_transition_by_tension(self):
        agent = Agent("A", state="Jaz")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("eno" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
