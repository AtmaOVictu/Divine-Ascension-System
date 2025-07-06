"""Ontological agent capable of emotional state transitions."""


class Agent:
    """Represent an agent with ontological states and emotional dynamics."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Starting ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
        tension:
            Initial tension level.
        emotion:
            Initial emotional intensity.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension accordingly."""
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            prefix = "Intenzivno čustveno odgovori: "
        elif self.emotion > 0.3:
            prefix = "Čustveno odgovori: "
        else:
            prefix = "Mirno odgovori: "

        return f"{prefix}{base}"

    def __str__(self) -> str:
        """Return a readable representation useful for debugging."""
        return f"{self.name} ({self.state}): Tension={self.tension}, Emotion={self.emotion}"
