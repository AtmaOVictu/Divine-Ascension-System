class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotional_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]

    def update_emotion(self, value: float, state: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity in the range ``0``-``1``.
        state:
            Optional textual emotional state (e.g. ``"happy"`` or ``"fearful"``).
        """
        self.emotion = value
        if state is not None:
            self.emotional_state = state
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        prefix_map = {
            "fearful": "S strahom pove, ",
            "angry": "Z jezo odgovori, ",
            "happy": "Veselo pravi, ",
            "neutral": "",
        }
        prefix = prefix_map.get(self.emotional_state, "")
        return prefix + base
