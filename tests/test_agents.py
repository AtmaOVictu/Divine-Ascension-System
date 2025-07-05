import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_parental_influence(self):
        birth = {"initial_tension": 0.2, "initial_emotion": 0.1}
        parents = {"parental_tension": 0.3, "parental_emotion": 0.2, "parental_pathos": 1}
        agent = Agent("B", birth_params=birth, parent_params=parents)
        self.assertGreaterEqual(agent.tension, 0.5)
        self.assertGreaterEqual(agent.emotion, 0.3)
        self.assertEqual(agent.pathos, 1)

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
