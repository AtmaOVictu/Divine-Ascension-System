import unittest
from divine_agents.tracker import OntologicalTracker


class TestOntologicalTracker(unittest.TestCase):
    def test_default_agents_exist(self):
        tracker = OntologicalTracker()
        self.assertIn("Mojster očesa", tracker.agents)
        self.assertIn("Mojster ušesa", tracker.agents)

    def test_initiate_interaction_triggers_transition(self):
        tracker = OntologicalTracker()
        state_before = tracker.agents["Mojster očesa"].state
        tracker.initiate_interaction(
            "Mojster očesa",
            "svet",
            emotion_delta=0.8,
            debate_topic="narava resnice",
        )
        new_state = tracker.agents["Mojster očesa"].state
        self.assertNotEqual(state_before, new_state)
        self.assertEqual(tracker.transitions[-1]["from"], state_before)


if __name__ == "__main__":
    unittest.main()
