class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in the range ``0``-``1``.
        name:
            Optional textual representation of the emotion (e.g. ``"fear"``).
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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
        """Return a philosophical answer influenced by emotion and state."""
        preface = ""
        if self.emotion_name == "fear":
            preface = "V strahu, "
        elif self.emotion_name == "joy":
            preface = "Z veseljem, "
        elif self.emotion_name == "anger":
            preface = "Z jezo, "

        if self.state == "Ego":
            return f"{preface}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{preface}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{preface}Vse resnice so eno, medsebojno povezane."
