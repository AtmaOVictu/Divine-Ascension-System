from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Track individual emotions that may influence tension
        self.emotions: Dict[str, float] = {"generic": emotion}

    def update_emotion(self, value: float, kind: str = "generic") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in range ``0``-``1``.
        kind:
            Name of the emotion (e.g. ``"fear"``, ``"joy"``, ``"anger"``).
        """
        self.emotions[kind] = value
        # Aggregate emotion intensity as the strongest current feeling
        self.emotion = max(self.emotions.values())

        # Fear and anger add tension, joy can calm the agent
        if kind in {"fear", "anger", "generic"}:
            self.tension += value
        elif kind == "joy":
            self.tension = max(0.0, self.tension - value / 2)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
