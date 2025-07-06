import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_only_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_multiple_state_changes(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")
        agent.update_tension(0.9)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure dialogue lines reflect ontological states
        self.assertTrue(any("Ego" in line for line in lines))
        self.assertTrue(any("Jaz" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
