"""Core logic for the ontological agents used in tests and simulations."""

from __future__ import annotations

import subprocess
from typing import List


class Agent:
    """Represent an ontological agent capable of philosophical transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def describe_emotion(self) -> str:
        """Return a textual representation of the current emotional state."""
        if self.emotion > 0.7:
            return "visoka"
        if self.emotion > 0.3:
            return "zmerna"
        return "nizka"

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."
        return f"{reply} (čustva: {self.describe_emotion()})"

    def log_to_github(self, message: str) -> None:
        """Attempt to create a git commit describing the agent's state."""
        commit_message = f"Agent {self.name}: {message}"
        try:
            subprocess.run(["git", "add", "-A"], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
        except Exception as exc:
            print(f"GitHub logging failed: {exc}")
