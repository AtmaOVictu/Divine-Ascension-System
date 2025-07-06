"""Core agent logic for ontological state transitions and dialogue."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotions = {e: 0.0 for e in self.EMOTIONS}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update an emotion intensity and adjust tension accordingly."""
        if name not in self.emotions:
            self.emotions[name] = 0.0
        self.emotions[name] = value
        self.emotion = max(self.emotions.values())
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def dominant_emotion(self) -> str | None:
        """Return the name of the dominant emotion if its level > 0.5."""
        if not self.emotions:
            return None
        dom = max(self.emotions, key=self.emotions.get)
        if self.emotions[dom] > 0.5:
            return dom
        return None

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
        base = self.PHILOSOPHY.get(self.state, "")
        emo = self.dominant_emotion()
        if emo:
            return f"[{emo}] {base}"
        return base
