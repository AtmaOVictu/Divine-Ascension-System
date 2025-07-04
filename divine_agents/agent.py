class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {}
        self.history = [state]
        self._refresh_emotion_level()

    def _refresh_emotion_level(self) -> None:
        self.emotion_level = max(self.emotions.values(), default=0.0)

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        self.emotions[emotion] = value
        self._refresh_emotion_level()
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        prefix = ""
        if self.emotion_level > 0.5:
            dominant = max(self.emotions, key=self.emotions.get)
            if dominant == "fear":
                prefix = "V strahu povem, "
            elif dominant == "joy":
                prefix = "Z veseljem povem, "
            elif dominant == "anger":
                prefix = "S jezo povem, "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}"
