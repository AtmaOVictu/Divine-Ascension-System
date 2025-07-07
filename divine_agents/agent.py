"""Ontological agents and logging utilities."""

import os
from datetime import datetime


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.version = self._generate_version()
        self.log_file = self._init_log_file()

    def _generate_version(self) -> str:
        """Generate a unique timestamp used for versioning."""
        return datetime.now().strftime("%Y%m%d%H%M%S%f")

    def _init_log_file(self) -> str:
        """Create a log file for the agent and write header info."""
        log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, f"{self.name}_log_{self.version}.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"Log Version: {self.version}\n")
            f.write(f"Agent: {self.name}\n")
            f.write(f"Start Time: {datetime.now()}\n\n")
        return log_path

    def _log(self, message: str) -> None:
        """Append a log entry with a timestamp."""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._log(f"Emotion updated to {self.emotion}; tension is {self.tension}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._log(f"Tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self._log(f"State transitioned to {self.state}")
        else:
            self._log("No transition: thresholds not met")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        elif self.state == "Enotnost":
            response = "Vse resnice so eno, medsebojno povezane."
        else:
            response = "Resnica je absolutna in neodvisna od drugih."
        self._log(f"Response: {response}")
        return response

    def save_history(self) -> None:
        """Persist the agent's state history to a file."""
        history_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        os.makedirs(history_dir, exist_ok=True)
        history_path = os.path.join(history_dir, f"{self.name}_history_{self.version}.txt")
        with open(history_path, "w", encoding="utf-8") as f:
            f.write(f"State History for {self.name}\n")
            for state in self.history:
                f.write(f"{state}\n")

