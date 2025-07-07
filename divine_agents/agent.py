from __future__ import annotations

import time


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.timestamp = time.time()
        self.version = self._generate_version()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _generate_version(self) -> str:
        """Return a time based version string."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _log(self, message: str) -> None:
        """Print a timestamped log message."""
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print(f"{ts} - {self.name}: {message}")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._log(f"Emotion updated to {self.emotion:.2f}, tension now {self.tension:.2f}")
        
    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._log(f"Tension set to {self.tension:.2f}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            prev_state = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            if self.state != prev_state:
                self._log(f"State transitioned from {prev_state} to {self.state}")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        influenced = self._apply_emotion_influence(msg)
        self._log(f"Responding with: {influenced}")
        return influenced

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _apply_emotion_influence(self, response: str) -> str:
        """Influence a response based on emotional intensity."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def save_history(self) -> None:
        """Persist the state history for later analysis."""
        file_name = f"{self.name}_history_{self.version}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"State History for {self.name}\n")
            for state in self.history:
                f.write(f"{state}\n")
