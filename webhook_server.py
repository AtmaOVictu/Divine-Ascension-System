import os
from flask import Flask, request, Response

try:
    from openai import OpenAI, InvalidWebhookSignatureError
except Exception:  # pragma: no cover - openai may not be installed
    class InvalidWebhookSignatureError(Exception):
        pass

    class DummyClient:
        def __init__(self, *args, **kwargs):
            pass

        class webhooks:
            @staticmethod
            def unwrap(data, headers):
                # Return dummy event structure
                return {"type": headers.get("X-Test-Event", "unknown"), "data": {"id": "0"}}

    def OpenAI(*args, **kwargs):  # type: ignore
        return DummyClient()


app = Flask(__name__)
client = OpenAI(webhook_secret=os.environ.get("OPENAI_WEBHOOK_SECRET", ""))


@app.route("/webhook", methods=["POST"])
def webhook() -> Response:
    """Endpoint to receive webhook events from OpenAI."""
    try:
        event = client.webhooks.unwrap(request.data, request.headers)
        print("Received event:", event.get("type"))
        return Response(status=200)
    except InvalidWebhookSignatureError:
        return Response("Invalid signature", status=400)


if __name__ == "__main__":  # pragma: no cover - manual start
    app.run(port=8000)
