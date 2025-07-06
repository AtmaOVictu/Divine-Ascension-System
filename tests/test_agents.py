import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Ego", emotion=0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("custva", reply)

    def test_key_activation(self):
        agent = Agent("A")
        agent.set_key("wisdom")
        self.assertEqual(agent.state, "Enotnost")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("custva" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
