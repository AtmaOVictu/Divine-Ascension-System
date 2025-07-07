class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Agent identifier.
    state: str
        Current ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension: float
        Internal tension influencing state transitions.
    emotion: float
        Intensity of the current emotion in range ``0..1``.
    emotion_name: str
        Name of the current emotion (``fear``, ``joy`` or ``anger``).
    history: list[str]
        Recorded history of states for debugging and analysis.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set the current emotion and adjust tension.

        Negative emotions (fear, anger) increase tension more than positive
        ones. Intensity should be between 0 and 1.
        """
        self.emotion_name = name
        self.emotion = intensity
        if name in {"fear", "anger"}:
            self.tension += intensity
        else:
            self.tension += intensity * 0.5

    # Backwards compatibility
    update_emotion = set_emotion

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
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name in {"fear", "anger"}:
            return f"{base} Občutim {self.emotion_name}."
        elif self.emotion_name != "neutral":
            return f"{base} Preveva me {self.emotion_name}."
        return base
