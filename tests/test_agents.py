import unittest
from divine_agents.agent import Agent, Emotion
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_when_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.5)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion("joy", 0.3)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("emocija: joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotional labels present
        self.assertTrue(any("emocija" in line for line in lines))

    def test_fear_returns_to_stable_axis(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion("fear", 0.2)
        self.assertEqual(agent.state, agent.stable_axis)


if __name__ == '__main__':
    unittest.main()
