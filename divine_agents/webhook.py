"""Simple webhook listener using built-in HTTP server."""

import os
import hmac
import hashlib
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Tuple

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "secret")


def verify_signature(payload: bytes, signature: str) -> bool:
    """Validate request signature."""
    computed = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)


def process_event(payload: bytes, signature: str) -> Tuple[int, str]:
    """Process webhook payload and return status code and message."""
    if not verify_signature(payload, signature):
        return 400, "Invalid signature"
    event = json.loads(payload.decode())
    if event.get("type") == "response.completed":
        output = event.get("data", {}).get("output", "")
        print("Response output:", output)
    return 200, ""


class WebhookHandler(BaseHTTPRequestHandler):
    """Minimal HTTP handler for webhook events."""

    def do_POST(self) -> None:  # noqa: N802 - naming convention from BaseHTTPRequestHandler
        length = int(self.headers.get("Content-Length", 0))
        payload = self.rfile.read(length)
        signature = self.headers.get("X-Signature", "")
        status, message = process_event(payload, signature)
        self.send_response(status)
        self.end_headers()
        if message:
            self.wfile.write(message.encode())


def run(port: int = 8000) -> None:
    """Run the webhook listener server."""
    server = HTTPServer(("", port), WebhookHandler)
    print(f"Webhook server listening on port {port}")
    server.serve_forever()
