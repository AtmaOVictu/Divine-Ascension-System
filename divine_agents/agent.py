class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier of the agent.
    state: str, optional
        Starting ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Initial tension level.
    emotion: float, optional
        Initial emotional intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion label.

        Parameters
        ----------
        value: float
            New emotional intensity.
        label: str, optional
            Descriptive emotion (e.g. ``"fear"``, ``"joy"``). If ``None`` the
            label is left unchanged.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        # Emotions contribute to rising tension
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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def speak(self, question: str) -> str:
        """Return a dialogue line influenced by emotion and state."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}, {self.emotion_label}): {answer}"
