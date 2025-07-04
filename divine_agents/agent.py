class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str
        Initial ontological state (``"Ego"`` by default).
    tension: float
        Initial tension level.
    emotion: float
        Initial emotion intensity.
    emotion_label: str
        Current emotional label (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion intensity and adjust tension via emotion influence."""
        self.emotion_label = label
        self.emotion = value
        if label in {"fear", "anger"}:
            self.tension += value
        elif label == "joy":
            self.tension = max(0.0, self.tension - value * 0.5)
        else:
            self.tension += value * 0.5

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
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = ""
        if self.emotion_label == "anger":
            prefix = "Z jezo povem: "
        elif self.emotion_label == "fear":
            prefix = "Z zaskrbljenostjo: "
        elif self.emotion_label == "joy":
            prefix = "Z veseljem: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
