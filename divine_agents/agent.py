class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and type.

        Increasing emotion also increases tension which may trigger a state
        transition in :meth:`transition`.
        """
        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The response is coloured by the agent's current emotion.
        """
        prefix = ""
        if self.emotion_type == "fear":
            prefix = "S strahom povem, "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem povem, "
        elif self.emotion_type == "anger":
            prefix = "Z jezo povem, "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
