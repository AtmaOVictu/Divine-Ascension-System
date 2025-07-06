class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_kind: str = "neutral") -> None:
        """Initialize agent with its ontological state and emotional context."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_kind = emotion_kind
        self.history = [state]

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotional intensity and type, adjusting tension."""
        self.emotion = value
        self.emotion_kind = kind
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
        """Return a philosophical answer influenced by the emotional state."""
        emotion_prefix = {
            "fear": "V strahu odgovarja:",
            "joy": "Z veseljem pravi:",
            "anger": "Z jezo odgovori:",
            "sorrow": "Žalostno pripomni:",
        }.get(self.emotion_kind, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}".strip()
