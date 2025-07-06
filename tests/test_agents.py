import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, debate_until_unity


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

    def test_emotion_influence(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("Čutim", response)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_until_unity(self):
        a1 = Agent("B1")
        a2 = Agent("B2")
        transcript = debate_until_unity(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
