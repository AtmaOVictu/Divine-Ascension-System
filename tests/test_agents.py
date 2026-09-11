import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.3)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        ego = Agent("E", state="Ego")
        self.assertIn("absolute", ego.respond("?"))

        jaz = Agent("J", state="Jaz")
        self.assertIn("relative", jaz.respond("?"))

        eno = Agent("N", state="Enotnost")
        self.assertIn("interconnected", eno.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("transitions" in line for line in lines))
        self.assertIn("absolute", lines[0])
        self.assertIn("relative", lines[1])


if __name__ == '__main__':
    unittest.main()
