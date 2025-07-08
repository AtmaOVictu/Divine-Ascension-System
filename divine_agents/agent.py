"""Agent implementation for ontological state transitions and dialogue."""

from .philosophy import State, PHILOSOPHICAL_TRUTHS


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(
        self,
        name: str,
        state: State = State.EGO,
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if label:
            self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return PHILOSOPHICAL_TRUTHS[self.state]

    def speak(self, question: str) -> str:
        """Return dialogue line with current emotional and ontological state."""
        response = self.respond(question)
        return f"{self.name} ({self.state.value}, {self.emotion_label}): {response}"
