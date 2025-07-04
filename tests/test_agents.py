import unittest
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
        agent.apply_emotion("joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_emotion_transition(self):
        agent = Agent("A")
        agent.apply_emotion("anger")
        agent.apply_emotion("fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any(state in line for state in ["Jaz", "Enotnost"] for line in lines))
        self.assertTrue(any("\u010custvo" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
