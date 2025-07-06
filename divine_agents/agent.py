class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique name for the agent.
    state:
        Ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level influencing transitions.
    emotion:
        Intensity of the current emotional feeling.
    emotion_type:
        Descriptive label of the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, emotion_type: str, intensity: float) -> None:
        """Set an emotional state and update tension accordingly."""
        self.emotion_type = emotion_type
        self.update_emotion(intensity)

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

        The emotional state adds flavor to the response.
        """
        prefix = ""
        if self.emotion_type == "fear":
            prefix = "Z zaskrbljenostjo pravim: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem pravim: "
        elif self.emotion_type == "anger":
            prefix = "Z jezo pravim: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
