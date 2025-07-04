import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import extended_dialogue


class TestExtendedDialogue(unittest.TestCase):
    def test_state_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = extended_dialogue(a1, a2, rounds=1)
        self.assertIn("A1 prehaja v stanje: Jaz", lines)
        self.assertIn("A2 prehaja v stanje: Enotnost", lines)

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("mo\u010dna", reply)


if __name__ == '__main__':
    unittest.main()
