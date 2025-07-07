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
        lines = philosophical_dialogue(a1, a2, ("joy", 0.8), ("anger", 0.6))
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("joy" in line for line in lines))
        self.assertTrue(any("anger" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
