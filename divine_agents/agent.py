class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
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
            return (
                "Truth is absolute and independent of others. "
                f"Emotion: {self.emotion:.2f}"
            )
        if self.state == "Jaz":
            return (
                "Truth is relative, shaped by our relationships. "
                f"Emotion: {self.emotion:.2f}"
            )
        return (
            "All truths are one, interconnected. "
            f"Emotion: {self.emotion:.2f}"
        )


class RespectAgent(Agent):
    """Agent that values respect and order."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return (
                "Respect is a foundational principle that maintains order. "
                f"Emotion: {self.emotion:.2f}"
            )
        return super().respond(question)


class DisrespectAgent(Agent):
    """Agent that disregards rules."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return (
                "Rules are meant to be broken, respect is an illusion. "
                f"Emotion: {self.emotion:.2f}"
            )
        return super().respond(question)


class FearAgent(Agent):
    """Agent influenced primarily by fear."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return (
                "Fear governs our choices; we act to avoid harm. "
                f"Emotion: {self.emotion:.2f}"
            )
        return super().respond(question)


class OneValueAgent(Agent):
    """Agent that bases decisions on a single value."""

    def __init__(self, name: str, value: float = 1.0, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.value = value

    def respond(self, question: str) -> str:
        if self.value > 0.5:
            return (
                "I make decisions based on my single value. "
                f"Emotion: {self.emotion:.2f}"
            )
        return "I don't see much beyond this."
