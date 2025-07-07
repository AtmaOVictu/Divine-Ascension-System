"""Agent and SubAgent classes for the Divine Ascension system."""

from __future__ import annotations

import time


class Agent:
    """Represents an ontological agent capable of transitioning states with logging."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.timestamp = time.time()
        self.version = self._generate_version()
        self.log_file = f"{self.name}_log_{self.version}.txt"
        self._initialize_log()

    # Logging utilities
    def _generate_version(self) -> str:
        """Generate a unique version identifier based on the timestamp."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _initialize_log(self) -> None:
        """Create the initial log file with basic information."""
        with open(self.log_file, "w") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(
                f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n\n"
            )

    def log(self, message: str) -> None:
        """Append a timestamped message to the log file."""
        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.timestamp))
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp_str} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension, and log the change."""
        self.emotion = value
        self.tension += value
        self.timestamp = time.time()
        self.log(f"Emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level and log the change."""
        self.tension = value
        self.timestamp = time.time()
        self.log(f"Tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and log it."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.timestamp = time.time()
        self.log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Generate a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."

        response = self.apply_emotion_influence(response)
        self.log(f"Response: {response}")
        return response

    def apply_emotion_influence(self, response: str) -> str:
        """Alter the response with an emotional tone based on intensity."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def save_history(self) -> None:
        """Persist state history to a versioned file."""
        history_file = f"{self.name}_history_{self.version}.txt"
        with open(history_file, "w") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")
