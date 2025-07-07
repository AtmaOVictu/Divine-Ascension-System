class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        """Initialize the agent with its ontological state and emotions."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        # store history as tuples of (from_state, to_state)
        self.history = [(state, None)]

    def update_emotion(self, intensity: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and type, adjusting tension.

        Parameters
        ----------
        intensity:
            New intensity of the emotion (0-1).
        emotion_type:
            Optional name of the emotion (e.g. ``"anger"``).
        """

        self.emotion = intensity
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # tension grows with emotional intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotional thresholds are exceeded."""
        previous_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append((previous_state, self.state))
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_note = {
            "anger": " Čutim jezo v tej razpravi.",
            "joy": " Veselim se tega razumevanja.",
            "fear": " Občutim strah ob teh mislih.",
        }.get(self.emotion_type, "")

        return base + emotion_note
