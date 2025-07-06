import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent_ego = Agent("A", state="Ego")
        self.assertIn("absolutna", agent_ego.respond("?"))

        agent_jaz = Agent("B", state="Jaz")
        self.assertIn("relativna", agent_jaz.respond("?"))

        agent_unity = Agent("C", state="Enotnost")
        self.assertIn("eno", agent_unity.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertTrue(any("Čutim" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
