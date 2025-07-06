import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import dialogue_with_opposites
from divine_agents.opposites import OntologicalOppositesGenerator


class TestOppositesGenerator(unittest.TestCase):
    def test_generate_opposites_returns_pair(self):
        gen = OntologicalOppositesGenerator()
        pair = gen.generate_opposites()
        self.assertEqual(len(pair), 2)
        self.assertIn(pair[0], gen.opposites)

    def test_create_transition_known_state(self):
        gen = OntologicalOppositesGenerator()
        result = gen.create_transition("ego")
        self.assertIn("ego", result)
        self.assertIn("jaz", result)

    def test_dialogue_with_opposites(self):
        gen = OntologicalOppositesGenerator()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dialogue_with_opposites(a1, a2, gen)
        self.assertTrue(any("Nasprotje:" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
