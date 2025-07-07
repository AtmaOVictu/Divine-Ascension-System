class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    a ``tension`` level and an ``emotion`` intensity.  ``emotion_label`` keeps
    track of the current predominant emotion which influences the textual
    response.  Transitions are triggered when ``tension`` is above ``0.7`` or
    ``emotion`` is above ``0.5``.
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

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str, value: float) -> None:
        """Set emotion label and intensity simultaneously."""
        self.emotion_label = label
        self.update_emotion(value)

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
        """Return a philosophical answer depending on the current state.

        The response is influenced by the current ``emotion_label`` which is
        prepended to the base ontological statement.
        """

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }.get(self.state, "")

        prefix = ""
        if self.emotion_label == "fear":
            prefix = "S \u010dustvom strahu izjavljam: "
        elif self.emotion_label == "joy":
            prefix = "Z radostjo povem: "
        elif self.emotion_label == "anger":
            prefix = "Z jezo razlagam: "

        return f"{prefix}{base}" if prefix else base
