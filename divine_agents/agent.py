class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: dict | None = None):
        self.name = name
        self.state = state if state in self.STATES else "Ego"
        self.tension = tension
        # track individual emotion intensities
        base = {e: 0.0 for e in self.EMOTIONS}
        if emotion:
            for k in base:
                base[k] = float(emotion.get(k, 0.0))
        self.emotion = base
        self.history = [self.state]

    def update_emotion(self, kind: str, value: float) -> None:
        """Update a single emotion and adjust tension accordingly."""
        if kind in self.emotion:
            self.emotion[kind] = value
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def emotion_level(self) -> float:
        """Return the intensity of the strongest emotion."""
        return max(self.emotion.values())

    def dominant_emotion(self) -> str:
        """Return the emotion with the highest intensity."""
        return max(self.emotion, key=self.emotion.get)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = {
            "fear": "Čutim strah,",
            "joy": "Čutim radost,",
            "anger": "Čutim jezo,",
        }[self.dominant_emotion()]
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {base}"
