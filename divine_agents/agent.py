class Agent:
    """Ontological agent capable of transitioning states and responding philosophically."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_intensity: float = 0.0, emotion_type: str = "neutral"):
        """Initialize the agent with a name, state and emotional parameters."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion type and intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self) -> str:
        """Return a philosophical answer based on the current state and emotion."""
        if self.state == "Ego":
            view = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            view = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            view = "Vse resnice so eno, medsebojno povezane."
        return f"{view} Čutim {self.emotion_type}."
