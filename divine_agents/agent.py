"""Core logic for ontological agents."""

from __future__ import annotations

from typing import List


def get_weather(location: str) -> str:
    """Placeholder weather retrieval function."""
    return f"The current weather in {location} is 25°C."


def send_email(to: str, body: str) -> str:
    """Placeholder email sender."""
    return f"Email sent to {to} with message: {body}"


class Agent:
    """Represents an ontological agent capable of transitioning states
    and performing actions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        mood: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood or "neutral"
        self.history: List[str] = [state]

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.mood = mood
        self.emotion = value
        if mood in ("fear", "anger"):
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current state and mood."""
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        tone = {
            "anger": " (izgovorjeno z jezo)",
            "fear": " (izgovorjeno s strahom)",
            "joy": " (izgovorjeno z veseljem)",
            "neutral": "",
        }.get(self.mood, "")

        return base + tone

    def execute_task(self, task: str, *args, **kwargs) -> str:
        """Handle functional tasks such as retrieving data or sending messages."""
        if task == "get_weather":
            return get_weather(*args, **kwargs)
        if task == "send_email":
            return send_email(*args, **kwargs)
        return "Task not recognized."
