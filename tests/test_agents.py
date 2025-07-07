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
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_response(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.7, "joy")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("radost", response)

    def test_dialogue_contains_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        joined = "\n".join(lines)
        self.assertIn("prehaja v stanje", joined)
        self.assertIn("resnica", joined.lower())


if __name__ == "__main__":
    unittest.main()
