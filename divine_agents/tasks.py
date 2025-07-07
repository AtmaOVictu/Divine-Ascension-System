from __future__ import annotations


def get_weather(location: str) -> str:
    """Return a mock weather report for the given location."""
    return f"The current weather in {location} is 25\N{DEGREE SIGN}C."


def send_email(to: str, body: str) -> str:
    """Mock function to simulate sending an email."""
    return f"Email sent to {to} with message: {body}"
