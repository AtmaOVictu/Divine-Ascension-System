import unittest
from divine_agents.onto_agent import OntoAgent, dynamic_dialogue


class TestOntoAgent(unittest.TestCase):
    def setUp(self):
        self.birth = {"initial_tension": 0.2, "initial_emotion": 0.1}
        self.parents = {
            "parental_tension": 0.3,
            "parental_emotion": 0.2,
            "parental_pathos": 0.1,
        }
        self.agent = OntoAgent("O", self.birth, self.parents)

    def test_birth_and_parental_values(self):
        self.assertAlmostEqual(self.agent.tension, 0.5)
        self.assertAlmostEqual(self.agent.emotion, 0.3)
        self.assertAlmostEqual(self.agent.pathos, 0.1)

    def test_optimized_transition(self):
        self.agent.update_tension(0.8)
        state = self.agent.optimize_transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        self.agent.update_emotion(0.8)
        response = self.agent.respond("Kaj je resnica?")
        self.assertIn("Močno čustvujem", response)

    def test_dynamic_dialogue(self):
        a2 = OntoAgent("B", self.birth, self.parents, state="Jaz")
        lines = dynamic_dialogue(self.agent, a2)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

