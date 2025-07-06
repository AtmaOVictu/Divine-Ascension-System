import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A", state="Jaz")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_include_emotion(self):
        agent = Agent("A", state="Jaz", emotion_label="sreca")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("sreca", reply)

    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
