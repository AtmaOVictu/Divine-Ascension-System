"""Ontological agents capable of philosophical state transitions."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TRANSITION_TENSION_THRESHOLD = 0.7
    TRANSITION_EMOTION_THRESHOLD = 0.5

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

    def emotion_descriptor(self) -> str:
        """Return a textual description of the current emotion level."""
        if self.emotion > 0.7:
            return "vznemirjeno"
        if self.emotion > 0.4:
            return "napeto"
        return "mirno"

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.tension > self.TRANSITION_TENSION_THRESHOLD
            or self.emotion > self.TRANSITION_EMOTION_THRESHOLD
        ):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            # calm the agent after transition
            self.tension = 0.0
            self.emotion = 0.0
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        mood = self.emotion_descriptor()
        if self.state == "Ego":
            return (
                f"{mood}, trdim, da je resnica absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"{mood}, menim, da je resnica relativna, oblikovana z našimi odnosi."
            )
        return f"{mood}, verjamem, da so vse resnice eno, medsebojno povezane."
