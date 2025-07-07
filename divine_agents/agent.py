import os
import time


class Agent:
    """Represents an ontological agent capable of transitioning states with logging."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, *, log_dir: str = "."):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.log_dir = log_dir
        self.timestamp = time.time()
        self.version = self._generate_version()
        self.log_file = os.path.join(self.log_dir, f"{self.name}_log_{self.version}.txt")
        self._initialize_log()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {self.emotion}")

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
        self.history.append(self.state)
        self.timestamp = time.time()
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
        response = self.apply_emotion_influence(response)
        self.log(f"Response: {response}")
        return response

    # ------------------------------------------------------------------
    # Logging utilities
    # ------------------------------------------------------------------

    def _generate_version(self) -> str:
        """Generate a unique version identifier based on the timestamp."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _initialize_log(self) -> None:
        """Create the log file and store initial metadata."""
        os.makedirs(self.log_dir, exist_ok=True)
        with open(self.log_file, "w", encoding="utf-8") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(
                f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n\n"
            )

    def log(self, message: str) -> None:
        """Append a timestamped message to the log file."""
        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.timestamp))
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(f"{timestamp_str} - {message}\n")

    def apply_emotion_influence(self, response: str) -> str:
        """Modify a response according to the agent's emotion."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def save_history(self) -> None:
        """Persist the agent's state history to disk."""
        history_file = os.path.join(self.log_dir, f"{self.name}_history_{self.version}.txt")
        with open(history_file, "w", encoding="utf-8") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")
