import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from webhook_server import app
except ModuleNotFoundError:
    app = None


class TestWebhook(unittest.TestCase):
    def setUp(self):
        if app is None:
            self.skipTest("Flask not installed")
        self.client = app.test_client()

    def test_webhook_success(self):
        response = self.client.post("/webhook", data=b"{}", headers={"X-Test-Event": "response.completed"})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
