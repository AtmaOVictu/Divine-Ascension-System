import unittest
from divine_agents.letters import create_letter_agents, letter_dialogue


class TestLetterAgents(unittest.TestCase):
    def test_create_agents(self):
        agents = create_letter_agents("AB")
        self.assertEqual(len(agents), 2)
        self.assertEqual(agents[0].name, "A")
        self.assertEqual(agents[1].state, "Ego")

    def test_letter_dialogue_transition(self):
        lines = letter_dialogue("AB")
        # Expect at least one transition line
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
