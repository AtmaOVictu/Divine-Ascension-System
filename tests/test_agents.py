import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "jeza")
        self.assertEqual(agent.transition(), "Jaz")

    def test_response_emotion_note(self):
        agent = Agent("A", state="Jaz", emotion_type="radovednost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("radovednost", reply)
        self.assertIn("relativna", reply)

    def test_dialogue_contains_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))
        self.assertTrue(any("Enotnost" in l for l in lines))


if __name__ == "__main__":
    unittest.main()
