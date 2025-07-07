class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: mapping of states to their philosophical principles
    PRINCIPLES = {
        "Ego": "Truth is absolute and independent of others.",
        "Jaz": "Truth is relative and shaped by our relationships.",
        "Enotnost": "All truths are one and interconnected.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New intensity of the emotion (0..1).
        kind:
            Optional name of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """

        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5 and self.emotion_type:
            return f"({self.emotion_type}) {base}"
        return base

    @staticmethod
    def ionize_word(word: str) -> str:
        """Return an \"ionized\" variant of ``word`` by shifting characters."""
        return "".join(chr(ord(ch) + 1) for ch in word)
