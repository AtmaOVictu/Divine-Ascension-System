from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history: List[str] = [state]
        self.potential_changes: List[str] = []

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity, adjust tension, and record the change."""
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        self.tension += value
        self.record_potential_change(f"emotion set to {value} ({self.emotion_label})")

    def update_tension(self, value: float) -> None:
        """Directly set tension level and record the change."""
        self.tension = value
        self.record_potential_change(f"tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.record_potential_change(f"transitioned to {self.state}")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"({self.emotion_label}) " if self.emotion_label != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

    def record_potential_change(self, change: str) -> None:
        """Record a potential change for hexdump-like tracking."""
        self.potential_changes.append(change)
