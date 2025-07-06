"""Core abstractions for ontological agents."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Initial ontological state (Ego, Jaz or Enotnost).
    tension:
        Initial level of tension in the agent.
    emotion:
        Current emotional intensity.
    """

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

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def _emotion_descriptor(self) -> str:
        """Return a simple textual description of the emotion level."""
        if self.emotion > 0.7:
            return "zelo čustveno"
        if self.emotion > 0.3:
            return "zmerno čustveno"
        return "mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        elif self.state == "Enotnost":
            answer = "Vse resnice so eno, medsebojno povezane."
        else:
            answer = "Neznana resnica."
        return f"{answer} ({self._emotion_descriptor()})"
