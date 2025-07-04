import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        initial_len = len(agent.history)
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(len(agent.history), initial_len + 1)

        agent.update_tension(0.1)
        agent.transition()
        self.assertEqual(len(agent.history), initial_len + 1)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
