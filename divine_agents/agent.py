class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique name of the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Initial tension level in the agent.
    emotion:
        Initial intensity of the current emotion.
    emotion_type:
        Descriptor of the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its descriptor.

        Parameters
        ----------
        value:
            New emotional intensity.
        emotion_type:
            Optional descriptor such as ``"fear"`` or ``"joy"``. When provided,
            ``emotion_type`` will be stored on the agent.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        The answer is prefixed with the agent's current emotional descriptor
        when one is available.
        """

        prefix = ""
        if self.emotion_type and self.emotion_type != "neutral":
            prefix = f"{self.emotion_type.capitalize()} občutek: "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
