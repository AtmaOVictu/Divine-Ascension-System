class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension value.
    emotion:
        Initial emotion intensity.
    emotion_name:
        Optional name of the emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "") -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        if name:
            self.emotion_name = name

        # Negative emotions increase tension, joy decreases it
        if self.emotion_name in {"fear", "anger", "sorrow"}:
            self.tension += value
        elif self.emotion_name == "joy":
            self.tension = max(0.0, self.tension - value)
        else:
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
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_prefix = f"Ob čustvu {self.emotion_name}, " if self.emotion_name else ""
        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
