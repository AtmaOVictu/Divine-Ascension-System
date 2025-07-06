class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotions = {}
        self.history = [state]

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion with the given intensity and update tension."""
        self.emotions[name] = intensity
        self.emotion = intensity
        if name in ("fear", "anger"):
            self.tension += intensity
        elif name == "joy":
            self.tension = max(0.0, self.tension - intensity / 2)

    def update_emotion(self, value: float) -> None:
        """Maintain backwards compatibility for updating emotion."""
        self.emotion = value
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_phrase = ""
        if self.emotions:
            last, intensity = max(self.emotions.items(), key=lambda e: e[1])
            if intensity > 0:
                if last == "fear":
                    emotion_phrase = "S strahom verjamem, da "
                elif last == "anger":
                    emotion_phrase = "Z jezo trdim, da "
                elif last == "joy":
                    emotion_phrase = "Z veseljem pravim, da "
        return f"{emotion_phrase}{base}"
