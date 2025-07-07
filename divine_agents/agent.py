import os
import time


class Agent:
    """Ontological agent capable of transitioning states with timestamped logs."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, log_dir: str = "."):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.log_dir = log_dir
        self.history = [state]
        self.timestamp = time.time()
        self.version = self._generate_version()
        self.log_file = os.path.join(self.log_dir,
                                     f"{self.name}_log_{self.version}.txt")
        self._initialize_log()

    def _generate_version(self) -> str:
        """Generate a unique version identifier based on time."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _initialize_log(self) -> None:
        """Create the initial log file with metadata."""
        with open(self.log_file, "w") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(
                f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n\n"
            )

    def _log(self, message: str) -> None:
        """Append a timestamped message to the log file."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.gmtime(self.timestamp))
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp_str} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.timestamp = time.time()
        self._log(f"Emotion updated to {self.emotion} | Tension {self.tension}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.timestamp = time.time()
        self._log(f"Tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Ego"
        self.history.append(self.state)
        self.timestamp = time.time()
        self._log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            response = (
                "Resnica je absolutna in neodvisna od drugih. (Ego)"
            )
        elif self.state == "Jaz":
            response = (
                "Resnica je relativna, oblikovana z našimi odnosi. (Jaz)"
            )
        else:
            response = "Vse resnice so eno, medsebojno povezane. (Enotnost)"

        response = self._apply_emotion_influence(response)
        self._log(f"Response: {response}")
        return response

    def _apply_emotion_influence(self, response: str) -> str:
        """Modify response based on the agent's current emotion."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def save_history(self) -> str:
        """Persist state history to an external file."""
        history_file = os.path.join(
            self.log_dir, f"{self.name}_history_{self.version}.txt")
        with open(history_file, "w") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")
        return history_file
