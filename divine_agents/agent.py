"""Agent module for ontological state transitions.

This module defines :class:`Agent` used in philosophical dialogues.  An
``Agent`` tracks its emotional intensity and tension level.  When either value
exceeds predefined thresholds the agent progresses through the ontological
states ``Ego`` -> ``Jaz`` -> ``Enotnost``.
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
        self.emotion_type = "neutral"

    EMOTION_IMPACT = {
        "fear": 0.6,
        "anger": 0.7,
        "joy": 0.3,
        "neutral": 0.0,
    }

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value * self.EMOTION_IMPACT.get(emotion_type, 0.0)

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

    def express_truth(self) -> str:
        """Compose a dialogue line reflecting state and emotion."""
        base = self.respond("Kaj je resnica?")
        if self.emotion_type == "anger":
            tone = "z jezo izjavi"
        elif self.emotion_type == "fear":
            tone = "prestavljeno s strahom"
        elif self.emotion_type == "joy":
            tone = "radostno pove"
        else:
            tone = "pove"
        return f"{self.name} ({self.state}) {tone}: {base}"
