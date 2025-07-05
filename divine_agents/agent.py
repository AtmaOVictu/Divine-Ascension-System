class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Create an agent.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_type:
            Descriptor of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            New intensity value. This also increases tension by the same amount.
        emotion_type:
            Optional descriptor for the current emotional tone.
        """
        self.emotion = float(value)
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += self.emotion

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = float(value)

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        match self.emotion_type:
            case "fear":
                emotion_part = " Čutim strah v sebi."
            case "joy":
                emotion_part = " Preveva me veselje."
            case "anger":
                emotion_part = " V meni tli jeza."
            case _:
                emotion_part = ""
        return f"{base}{emotion_part}"
