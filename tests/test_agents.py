import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_emotion_based_transition(self):
        agent = Agent("B")
        agent.feel("anger", 2.0)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_in_response(self):
        agent = Agent("C")
        agent.feel("fear", 1.0)
        agent.transition()
        response = agent.respond("Kaj je resnica?")
        self.assertIn("fear", response)

    def test_philosophical_debate(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        transcript = philosophical_debate(a1, a2, rounds=1)
        self.assertGreaterEqual(len(transcript), 4)


if __name__ == '__main__':
    unittest.main()
