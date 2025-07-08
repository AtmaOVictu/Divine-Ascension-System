"""Core agent logic for ontological transitions and responses."""

from .philosophy import State, PRINCIPLES


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(
        self,
        name: str,
        state: State = State.EGO,
        tension: float = 0.0,
        emotion_level: float = 0.0,
        emotion_type: str = "neutral",
    ):
        self.name = name
        self.state: State = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_level = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = PRINCIPLES[self.state]
        mood = {
            "fear": "Z zaskrbljenostjo",
            "joy": "Z veseljem",
            "anger": "Z jezo",
        }.get(self.emotion_type, "")
        prefix = f"{mood}, " if mood else ""
        return f"{prefix}{base}"
