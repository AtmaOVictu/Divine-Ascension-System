import os
from datetime import datetime


class Agent:
    """Represents an ontological agent capable of transitioning states and logging actions."""

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

    def _generate_version(self) -> str:
        """Generate a unique version identifier based on time."""
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def _initialize_log(self) -> None:
        """Create the log file with initial metadata."""
        with open(self.log_file, "w") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(f"Start Time: {datetime.now()}\n\n")

    def log(self, message: str) -> None:
        """Append a timestamped message to the log file."""
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {self.emotion}; tension is now {self.tension}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension updated to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        self.log(f"Response: {response}")
        return response

    def save_history(self) -> None:
        """Save the agent's state history to a separate file."""
        history_file = f"{self.name}_history_{self.version}.txt"
        with open(history_file, "w") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")
