import unittest
import random
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
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_random_response(self):
        random.seed(0)
        agent = Agent("R", use_random=True)
        reply = agent.respond("Kaj je resnica?")
        options = [
            "Resnica je absolutna in neodvisna od drugih.",
            "Resnica je neodvisna od drugih.",
        ]
        self.assertIn(reply, options)

    def test_emotion_affects_response(self):
        agent = Agent("E")
        agent.update_emotion(0.6, "veselje")
        agent.transition()
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)


if __name__ == '__main__':
    unittest.main()
