from __future__ import annotations

import os
from datetime import datetime


class Agent:
    """Represents an ontological agent capable of transitioning states and logging.

    Each agent keeps a log of its state transitions and responses which can later
    be inspected by sub-agents for sorting or analysis."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        self.version = self._generate_version()
        self.log_file = f"{self.name}_log_{self.version}.txt"
        self._initialize_log()

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def _generate_version(self) -> str:
        """Generate a unique version identifier based on time."""
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def _initialize_log(self) -> None:
        """Create a log file with basic header information."""
        with open(self.log_file, "w", encoding="utf-8") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(f"Start Time: {datetime.now()}\n\n")

    def log(self, message: str) -> None:
        """Append a timestamped message to the agent's log file."""
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {self.emotion}; tension is now {self.tension}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.log(f"State transitioned to {self.state}")
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
        self.log(f"Response: {reply}")
        return reply

    def save_history(self) -> None:
        """Persist the agent's state history to disk."""
        history_file = f"{self.name}_history_{self.version}.txt"
        with open(history_file, "w", encoding="utf-8") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")

