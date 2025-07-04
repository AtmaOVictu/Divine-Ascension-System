import unittest
from divine_agents import Agent, philosophical_dialogue, debate


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

    def test_emotion_influence(self):
        agent = Agent("B", emotion=0.8, emotion_type="fear")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("fear", response)

    def test_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = debate(a1, a2, rounds=2)
        self.assertTrue(len(lines) >= 4)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
