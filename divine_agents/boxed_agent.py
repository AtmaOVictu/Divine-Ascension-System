from .agent import Agent
from .box import SymbolicBox


class BoxedAgent(Agent):
    """Agent aware of its own boxed state and emotions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str = "neutral"):
        super().__init__(name, state, tension, emotion)
        self.emotion_type = emotion_type
        self.self_box = SymbolicBox(stage="∴", data={"identity": name, "state": state})

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:  # type: ignore[override]
        """Update emotion intensity, emotion type, and adjust tension."""
        self.emotion_type = emotion_type
        super().update_emotion(value)
        if emotion_type in {"fear", "anger"}:
            self.tension += 0.1

    def transition(self) -> str:  # type: ignore[override]
        """Perform transition and update the internal box."""
        previous = self.state
        new_state = super().transition()
        if new_state != previous:
            self.self_box.transition("∆", {"state": new_state})
        return new_state

    def respond(self, question: str) -> str:  # type: ignore[override]
        base = super().respond(question)
        return f"{base} (čustvo: {self.emotion_type})"
