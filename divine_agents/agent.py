class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Current tension level.
    emotion: float
        Intensity of the current emotion.
    emotion_name: str
        Name of the current emotion (e.g. ``fear``, ``joy``).
    history: list[str]
        History of all states the agent has gone through.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, name: str, value: float) -> None:
        """Set emotion name and intensity, adjusting tension."""
        self.emotion_name = name
        self.update_emotion(value)
        if name in ("fear", "anger"):
            self.tension += value
        else:
            self.tension += value / 2

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
        prefix = {
            "fear": "S strahom odgovarjam, ",
            "anger": "Z jezo odgovarjam, ",
            "joy": "Veselo povem, ",
        }.get(self.emotion_name, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}".strip()
