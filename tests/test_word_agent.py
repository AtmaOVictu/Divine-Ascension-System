import unittest

from divine_agents.word_agent import WordAgent
from divine_agents.library import create_word_library


class TestWordAgent(unittest.TestCase):
    def test_activation_and_transition(self):
        agent = WordAgent("Resnica")
        self.assertEqual(agent.state, "inactive")
        agent.activate()
        self.assertEqual(agent.state, "active")
        self.assertEqual(agent.energy, 0.5)

        state = agent.transition()
        self.assertEqual(state, "energized")
        self.assertEqual(agent.energy, 1.0)

        state = agent.transition()
        self.assertEqual(state, "resonating")

    def test_create_library(self):
        words = ["Resnica", "Dobro"]
        library = create_word_library(words)
        self.assertEqual(len(library), 2)
        self.assertTrue(all(isinstance(w, WordAgent) for w in library))


if __name__ == "__main__":
    unittest.main()
