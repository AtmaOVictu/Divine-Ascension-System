class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Nujnost")

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

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value
        self.check_for_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for transition."""
        self.tension = value
        self.check_for_transition()

    def check_for_transition(self) -> None:
        """Check if tension or emotion exceeds the limit and reset if needed."""
        if self.tension >= 1.0 or self.emotion >= 1.0:
            self.transition_to_unity()

    def transition_to_unity(self) -> None:
        """Transition to 'Enotnost' when the tension or emotion is at max."""
        if self.state != "Enotnost":
            self.state = "Enotnost"
            self.history.append(self.state)
            self.reset_agent()

    def reset_agent(self) -> None:
        """Reset agent to a new urgency state after reaching unity."""
        self.state = "Nujnost"
        self.tension = 0.0
        self.emotion = 0.0
        self.history.append(self.state)

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return "Vrnitev v stanje nujnosti omogo\u010da nov za\u010detek."

    def __str__(self) -> str:
        return (
            f"{self.name} is in state {self.state} with "
            f"emotion {self.emotion_type} and tension {self.tension:.2f}"
        )
