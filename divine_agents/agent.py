from typing import Dict, Tuple


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotions: Dict[str, float] | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {}
        self.history = [state]

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set an emotion and adjust tension accordingly."""
        self.emotions[label] = intensity
        self.tension += intensity

    def current_emotion(self) -> Tuple[str, float] | tuple[None, float]:
        """Return the strongest emotion if present."""
        if not self.emotions:
            return (None, 0.0)
        emotion = max(self.emotions.items(), key=lambda x: x[1])
        return emotion

    # Backwards compatibility with previous API
    def update_emotion(self, value: float) -> None:
        self.set_emotion("neutrino", value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        strongest_emotion = self.current_emotion()[1]
        if self.tension > 0.7 or strongest_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        label, intensity = self.current_emotion()
        if label and intensity > 0:
            return f"Ob čustvu {label} ({intensity:.1f}) pravim: {base}"
        return base
