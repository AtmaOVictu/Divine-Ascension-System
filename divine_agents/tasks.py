"""Utility functions representing external tasks."""


def get_weather(location: str) -> str:
    """Return mock weather information for the given location."""
    return f"Trenutno vreme v {location} je 25°C."


def send_email(to: str, body: str) -> str:
    """Simulate sending an email and return confirmation."""
    return f"E-pošta poslana na {to} z vsebino: {body}"

