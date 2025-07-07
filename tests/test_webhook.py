import json
import hmac
import hashlib
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.webhook import process_event


class TestWebhookProcessing(unittest.TestCase):
    def setUp(self):
        os.environ['WEBHOOK_SECRET'] = 'secret'

    def sign(self, payload: bytes) -> str:
        return hmac.new(b'secret', payload, hashlib.sha256).hexdigest()

    def test_valid_signature(self):
        payload = json.dumps({
            "type": "response.completed",
            "data": {"output": "hello"}
        }).encode()
        status, _ = process_event(payload, self.sign(payload))
        self.assertEqual(status, 200)

    def test_invalid_signature(self):
        payload = b'{}'
        status, message = process_event(payload, 'bad')
        self.assertEqual(status, 400)
        self.assertEqual(message, 'Invalid signature')


if __name__ == '__main__':
    unittest.main()
