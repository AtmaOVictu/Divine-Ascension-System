class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Ontological state: ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Current tension level.
    emotion_intensity:
        Numeric representation of the current emotional intensity.
    emotion:
        Name of the emotion influencing the agent.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_intensity: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, intensity: float, emotion: str | None = None) -> None:
        """Update emotion intensity and optionally emotion name.

        The agent's tension is increased by the emotion intensity.
        """
        self.emotion_intensity = intensity
        if emotion is not None:
            self.emotion = emotion
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
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

        if self.emotion != "neutral":
            base = f"{base} Čutim {self.emotion}."
        return base
