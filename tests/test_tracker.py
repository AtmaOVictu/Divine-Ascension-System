import unittest
from divine_agents import OntologicalTracker


class TestOntologicalTracker(unittest.TestCase):
    def test_default_agents(self):
        tracker = OntologicalTracker()
        self.assertEqual(len(tracker.agents), 4)

    def test_interaction_triggers_transition(self):
        tracker = OntologicalTracker()
        prev_state = tracker.agents["Mojster očesa"].state
        tracker.interact("Mojster očesa", "Kaj je resnica?", 0.8)
        new_state = tracker.agents["Mojster očesa"].state
        self.assertNotEqual(prev_state, new_state)
        self.assertTrue(any(t['agent'] == "Mojster očesa" for t in tracker.transitions))


if __name__ == '__main__':
    unittest.main()
