import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

        agent2 = Agent("B", state="Jaz")
        agent2.update_tension(0.9)
        self.assertEqual(agent2.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion(0.9)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("močnim", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertGreaterEqual(len(lines), 4)


if __name__ == '__main__':
    unittest.main()
