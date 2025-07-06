class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Initial tension level which influences state transitions.
    emotion_intensity:
        Strength of the current emotional state.
    emotion_type:
        Descriptive label for the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_intensity: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion intensity and type and adjust tension accordingly."""

        self.emotion_type = emotion_type
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotion or tension cross thresholds."""

        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""

        emotion_prefix = {
            "fear": "V strahu odgovarjam:",
            "joy": "Z veseljem odgovarjam:",
            "anger": "Z jezo odgovarjam:",
            "neutral": "Mirno odgovarjam:",
        }.get(self.emotion_type, "Odgovarjam:")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{emotion_prefix} {base}"
