import unittest

from divine_agents.ontological import OntologicalAgent, OppositeAgent


class TestOntologicalDebate(unittest.TestCase):
    def test_define_opposite_and_debate(self):
        ego = OntologicalAgent("Ego", concept="self-centered")
        jaz = OppositeAgent("Jaz", concept="relational identity")
        ego.define_opposite(jaz)

        lines = ego.debate()
        self.assertTrue(lines)
        self.assertIn("dialekti", lines[0])
        self.assertEqual(ego.state, "Jaz")
        self.assertIn("Jaz", ego.history[-1])

    def test_transition_thresholds(self):
        agent = OntologicalAgent("A", concept="concept", tension=0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == "__main__":
    unittest.main()
