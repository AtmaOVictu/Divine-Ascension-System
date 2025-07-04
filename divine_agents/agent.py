"""Ontological agents and state management."""

class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent moves through the states ``Ego`` -> ``Jaz`` -> ``Enotnost``. The
    transition is triggered when either the ``tension`` exceeds ``0.7`` or the
    ``emotion`` exceeds ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        return self.PHILOSOPHY.get(self.state, "")

    def speak_about_truth(self) -> str:
        """Return a dialogue line reflecting state and emotion."""
        emotion_pct = int(self.emotion * 100)
        statement = self.respond("Kaj je resnica?")
        return f"{self.name} ({self.state}, {emotion_pct}% emotion): {statement}"
