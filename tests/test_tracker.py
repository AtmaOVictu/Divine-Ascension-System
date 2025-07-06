import unittest

from divine_agents import OntologicalTracker


class TestOntologicalTracker(unittest.TestCase):
    def test_interaction_triggers_transition(self):
        tracker = OntologicalTracker()
        result = tracker.initiate_interaction(
            "Mojster očesa", "slika", emotion=0.8
        )
        self.assertIn("Mojster očesa zaznava", result)
        self.assertEqual(tracker.agents["Mojster očesa"].state, "Jaz")
        self.assertTrue(tracker.transitions)


if __name__ == "__main__":
    unittest.main()
