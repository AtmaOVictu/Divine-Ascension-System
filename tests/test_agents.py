import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentSystem(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.8, "strah")
        self.assertEqual(agent.transition(), "Jaz")

    def test_response_emotional_prefix(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "veselje")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z veseljem"))

    def test_dialogue_outcome(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        joined = "\n".join(lines)
        self.assertIn("Enotnost", joined)
        self.assertTrue(any("S strahom" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
