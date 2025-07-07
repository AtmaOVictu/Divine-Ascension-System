class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Nujnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str = "neutral") -> None:
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
        """Directly set tension level and trigger transition check."""
        self.tension = value
        self.check_for_transition()

    def check_for_transition(self) -> None:
        """Check for unity transition when limits are reached."""
        if self.tension >= 1.0 or self.emotion >= 1.0:
            self.transition_to_unity()

    def transition_to_unity(self) -> None:
        """Move to 'Enotnost' and reset the agent."""
        if self.state != "Enotnost":
            self.state = "Enotnost"
            self.history.append(self.state)
        self.reset_agent()

    def reset_agent(self) -> None:
        """Reset the agent to the 'Nujnost' state after reaching unity."""
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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion_type})"

    def __str__(self) -> str:
        return f"{self.name} is in state {self.state} with emotion {self.emotion_type} " \
               f"and tension {self.tension:.2f}"
