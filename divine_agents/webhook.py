from flask import Flask, request, Response


def process_event(event):
    """Process incoming webhook event."""
    event_type = event.get("type")
    if event_type == "response.completed":
        return "Processed response"
    return "Unknown event"


def create_app():
    """Create Flask app with webhook endpoint."""
    app = Flask(__name__)

    @app.route('/webhook', methods=['POST'])
    def webhook():
        event = request.get_json(force=True)
        process_event(event)
        return Response(status=200)

    return app
