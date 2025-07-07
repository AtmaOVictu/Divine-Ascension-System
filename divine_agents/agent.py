class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Nujnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity, its type and adjust tension."""
        self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value
        self.check_for_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for mandatory transitions."""
        self.tension = value
        self.check_for_transition()

    def check_for_transition(self) -> None:
        """Auto transition to unity if maximum values are reached."""
        if self.tension >= 1.0 or self.emotion >= 1.0:
            self.transition_to_unity()

    def transition_to_unity(self) -> None:
        """Move into 'Enotnost' and immediately reset to 'Nujnost'."""
        if self.state != "Enotnost":
            self.state = "Enotnost"
            self.history.append(self.state)
            self.reset_agent()

    def reset_agent(self) -> None:
        """Reset agent after reaching unity."""
        self.state = "Nujnost"
        self.tension = 0.0
        self.emotion = 0.0
        self.emotion_type = "neutral"
        self.history.append(self.state)

    def transition(self) -> str:
        """Perform sequential state transitions based on thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Nujnost":
                self.state = "Ego"
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
        return "Iskanje novih resnic se šele začenja."

    def __str__(self) -> str:
        return (f"{self.name} is in state {self.state} with emotion "
                f"{self.emotion_type} and tension {self.tension:.2f}")
