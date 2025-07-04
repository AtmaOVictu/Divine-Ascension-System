import unittest
from divine_agents.agent import Agent
from divine_agents.interaction import philosophical_debate


class TestPhilosophicalDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        # After debate A1 should have transitioned to Jaz
        self.assertEqual(a1.state, "Jaz")
        # A2 should reach Enotnost due to emotion threshold
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotional_prefix(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        response = agent.respond("Kaj je resnica?")
        self.assertTrue(response.startswith("Strastno"))


if __name__ == "__main__":
    unittest.main()
