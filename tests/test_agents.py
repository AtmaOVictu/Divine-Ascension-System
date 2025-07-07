import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_influence(self):
        agent = Agent("B", tension=0.5)
        agent.update_emotion("joy", 0.4)
        self.assertLess(agent.tension, 0.5)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion("anger", 0.7)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("jezno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("govori" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
