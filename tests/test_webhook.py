import unittest
from divine_agents.webhook import create_app, process_event


class TestWebhook(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_process_event(self):
        result = process_event({"type": "response.completed"})
        self.assertIn("Processed", result)

    def test_webhook_route(self):
        resp = self.app.post("/webhook", json={"type": "response.completed"})
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
