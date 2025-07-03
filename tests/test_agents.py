import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate


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

    def test_no_transition_with_low_values(self):
        agent = Agent("B")
        agent.update_tension(0.2)
        agent.update_emotion(0.3)
        self.assertEqual(agent.transition(), "Ego")

    def test_dynamic_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = dynamic_debate(a1, a2, rounds=2, emotion_increment=0.6)
        self.assertEqual(a1.state, "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
