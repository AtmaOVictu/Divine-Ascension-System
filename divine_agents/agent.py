class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Current tension level in the agent.
    emotion:
        Current emotion intensity.
    emotion_type:
        Descriptive label of the current emotion (e.g. ``"fear"`` or ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and type and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
        # Emotions directly influence tension accumulation
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
        """Return a philosophical answer influenced by the agent's state and emotion."""
        prefix = {
            "fear": "S strahom",
            "anger": "Z jezo",
            "joy": "Z veseljem",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix} {core}".strip()
