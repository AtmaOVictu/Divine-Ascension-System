class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level in the range ``0-1``.
    emotion:
        Initial emotion intensity in the range ``0-1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    TRANSITION_TENSION = 0.7
    TRANSITION_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name: str | None = None
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.apply_emotion("neutral", value)

    def apply_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion and modify tension based on its intensity."""
        self.emotion_name = name
        self.emotion = intensity
        if name in {"fear", "anger", "sorrow"}:
            self.tension += intensity
        elif name == "joy":
            self.tension = max(0.0, self.tension - intensity)
        else:
            self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TRANSITION_TENSION or self.emotion > self.TRANSITION_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"[{self.emotion_name}] " if self.emotion_name else ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
