class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        The name of the agent.
    state: str
        One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension: float
        Current tension level of the agent.
    emotion: float
        Intensity of the current emotional state.
    emotion_name: str
        Descriptive name of the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, value: float) -> None:
        """Assign an emotion by name and adjust tension."""
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

    @property
    def principle(self) -> str:
        """Return a short statement of the current philosophical principle."""
        if self.state == "Ego":
            return "Truth is absolute."
        if self.state == "Jaz":
            return "Truth is relative."
        return "All truths are unified."
