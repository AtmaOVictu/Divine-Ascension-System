from typing import Optional


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TRUTHS = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def philosophical_principle(self) -> str:
        """Return the core philosophical principle of the current state."""
        return self.TRUTHS[self.state]

    def respond(self, question: str = "") -> str:
        """Return an answer influenced by current state and emotion."""
        base = self.philosophical_principle()
        if self.emotion > 0.5 and self.emotion_type:
            return f"{base} (čustvo: {self.emotion_type})"
        return base
