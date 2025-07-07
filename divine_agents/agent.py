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
        """Set emotion intensity and adjust tension.

        Parameters
        ----------
        value : float
            New emotion intensity in the range ``0.0`` to ``1.0``.

        Raises
        ------
        ValueError
            If ``value`` is negative.
        """
        if value < 0.0:
            raise ValueError("Emotion value cannot be negative")
        self.emotion = value
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Set the agent's tension level.

        Parameters
        ----------
        value : float
            Desired tension in the range ``0.0`` to ``1.0``.
        """
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform state transition when emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            tone = " Moja čustva so silovita."
        elif self.emotion > 0.4:
            tone = " Občutim rahlo nihanje."
        else:
            tone = ""
        return base + tone
