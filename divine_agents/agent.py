class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Initialize the agent.

        Parameters
        ----------
        name: str
            Name of the agent.
        state: str
            Initial ontological state.
        tension: float
            Base tension level.
        emotion: float
            Intensity of the current emotion.
        emotion_type: str
            Descriptor of the current emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and adjust tension.

        Fear and anger increase tension while joy slightly decreases it.
        """
        self.emotion_type = emotion_type
        self.emotion = intensity
        if emotion_type in {"fear", "anger"}:
            self.tension += intensity
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - intensity / 2)
        else:
            self.tension += intensity

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        # Emotion influences the tone of the response
        if self.emotion_type == "fear":
            return f"{base} Občutim strah."
        if self.emotion_type == "anger":
            return f"{base} Čutim jezo."
        if self.emotion_type == "joy":
            return f"{base} Preveva me veselje."
        return base
