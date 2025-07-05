import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "RES000")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_full_transition_sequence(self):
        agent = Agent("A")
        expected = ["RES000", "RES001", "RES002", "RES003", "Jaz", "Enotnost"]
        for state in expected:
            agent.update_emotion(0.8, "test")
            self.assertEqual(agent.transition(), state)


if __name__ == '__main__':
    unittest.main()
