import unittest
from divine_agents.information import InformationControl, InformationGatherer


class TestInformation(unittest.TestCase):
    def test_filtering(self):
        ctrl = InformationControl(max_data_limit=2)
        ctrl.update_emotion("anger")
        data = [
            {"urgency": True},
            {"urgency": False},
        ]
        filtered = ctrl.gather_data(data)
        self.assertEqual(len(filtered), 1)

    def test_gatherer_web_search(self):
        g = InformationGatherer()
        results = g.search_web("test", emotional_state="calm")
        self.assertIn("detailed analysis", results)


if __name__ == "__main__":
    unittest.main()
