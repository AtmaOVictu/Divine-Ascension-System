class Agent:
    """Ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = {}
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Set emotion intensity and adjust tension."""
        self.emotions[name] = intensity
        self.tension += intensity

    def dominant_emotion(self) -> tuple[str, float]:
        """Return the dominant emotion and its intensity."""
        if not self.emotions:
            return ("neutral", 0.0)
        emotion = max(self.emotions.items(), key=lambda kv: kv[1])
        return emotion

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def overall_emotion(self) -> float:
        """Return highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.overall_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        emotion, intensity = self.dominant_emotion()
        prefix = "" if intensity <= 0.5 else f"Z občutkom {emotion} "
        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core
