class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Identifier of the agent.
    state: str
        Current ontological state (Ego, Jaz or Enotnost).
    tension: float
        Current tension level which influences transitions.
    emotion: float
        Intensity of the dominant emotion. Higher values increase tension.
    emotion_name: str
        Name of the dominant emotion affecting the agent.
    history: list[str]
        Chronological list of states for introspection and testing.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, value: float) -> None:
        """Set a named emotion and adjust tension."""
        self.emotion_name = name
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def __repr__(self) -> str:
        return (
            f"Agent(name={self.name!r}, state={self.state!r}, "
            f"tension={self.tension:.2f}, emotion={self.emotion:.2f}, "
            f"emotion_name={self.emotion_name!r})"
        )
