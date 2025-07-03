"""Core logic for ontological agents.

Agents transition between philosophical states depending on their
current ``emotion`` and ``tension``.  A transition occurs when either
``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.  Each
state represents a different view on truth:

``Ego``
    Truth is absolute and independent of others.

``Jaz``
    Truth is relative and shaped through relationships.

``Enotnost``
    All truths are one and interconnected.
"""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

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

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        base = self.PHILOSOPHY.get(self.state, "")
        # Strong emotions make the answer more emphatic
        if self.emotion > 0.7:
            return f"{base}!"
        return base
