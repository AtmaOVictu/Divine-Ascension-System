"""Ontological agent implementation.

Each agent can transition between three philosophical states based on the
current emotional intensity and tension.  The thresholds for transitions are
driven directly by the project requirements:

``tension`` must exceed ``0.7`` **or** ``emotion`` must exceed ``0.5`` to allow
movement from ``Ego`` -> ``Jaz`` or ``Jaz`` -> ``Enotnost``.
"""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension = max(self.tension, value)

    def increase_emotion(self, delta: float) -> None:
        """Increase emotion by ``delta`` and raise tension accordingly."""
        self.emotion = min(1.0, self.emotion + delta)
        self.tension += delta

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion > 0.7:
            return f"{base} (izraženo s strastjo)"
        if self.emotion > 0.3:
            return f"{base}"
        return base
