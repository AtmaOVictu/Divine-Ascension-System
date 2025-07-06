class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str
        Ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Current tension level between ``0`` and ``1``.
    emotion: float
        Numerical representation of emotion intensity between ``0`` and ``1``.
    emotion_state: str
        Descriptive emotion (e.g. ``fear``, ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state
        self.history = [state]

    def update_emotion(self, value: float, emotion_state: str | None = None) -> None:
        """Update emotion intensity and optionally the named emotional state."""
        self.emotion = value
        if emotion_state is not None:
            self.emotion_state = emotion_state
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
        """Return a philosophical answer depending on the current and emotional state."""
        emotion_note = {
            "fear": "Čutim strah.",
            "joy": "Občutim veselje.",
            "anger": "Preveva me jeza.",
        }.get(self.emotion_state, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} {emotion_note}".strip()
