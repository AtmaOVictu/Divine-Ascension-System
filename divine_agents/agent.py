import time


class Agent:
    """Ontological agent capable of transitioning states with timestamped logs."""

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

    def _generate_version(self) -> str:
        """Generate a unique version identifier based on creation time."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _initialize_log(self) -> None:
        """Create the initial log file for the agent."""
        with open(self.log_file, "w") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n\n")

    def _log(self, message: str) -> None:
        """Append a message with the current timestamp to the log file."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp_str} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension, logging the change."""
        self.emotion = value
        self.tension += value
        self._log(f"Emotion updated to {self.emotion}")

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
        self.history.append(self.state)
        self.timestamp = time.time()
        self._log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        response = self._apply_emotion_influence(base)
        self._log(f"Response: {response}")
        return response

    def _apply_emotion_influence(self, response: str) -> str:
        """Modify response according to current emotion level."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def save_history(self) -> None:
        """Write the agent's state history to an external file."""
        history_file = f"{self.name}_history_{self.version}.txt"
        with open(history_file, "w") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")
        self._log(f"History saved to {history_file}")
        return history_file
