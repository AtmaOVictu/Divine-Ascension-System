"""Core agent module handling ontological state transitions and replies."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    # ------------------------------------------------------------------
    # emotional and tension mechanics
    # ------------------------------------------------------------------
    def apply_emotion(self, value: float) -> None:
        """Apply an emotion value which increases tension.

        Parameters
        ----------
        value: float
            Intensity of the emotion in the range ``0.0`` to ``1.0``.
        """

        self.emotion = max(0.0, min(value, 1.0))
        self.tension = max(0.0, min(self.tension + value, 1.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = max(0.0, min(value, 1.0))

    # ------------------------------------------------------------------
    # transition and responses
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current state and emotion."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"Čutim močna čustva. {base}"
        return base
