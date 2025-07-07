class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent keeps track of its current ontological state, emotional
    intensity and type, as well as tension which is influenced by emotions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotional type and intensity."""
        self.emotion_type = emotion_type
        self.update_emotion(intensity)

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
        """Return a philosophical answer depending on the current state.

        The answer also reflects the current emotional tone of the agent.
        """
        prefix = {
            "fear": "(prestra\u0161eno)",
            "joy": "(veselo)",
            "anger": "(jezno)",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {core}".strip()
