import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.9, "anger")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Vse resnice", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue agent2 should transition to Enotnost
        self.assertIn("Enotnost", a2.state)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
