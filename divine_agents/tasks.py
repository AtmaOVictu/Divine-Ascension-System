"""Utility tasks for agents to execute as external actions."""

from __future__ import annotations


def get_weather(location: str) -> str:
    """Mock function returning weather information for a location."""
    return f"The current weather in {location} is 25\u00b0C."


def send_email(to: str, body: str) -> str:
    """Mock function simulating sending an email."""
    return f"Email sent to {to} with message: {body}"
