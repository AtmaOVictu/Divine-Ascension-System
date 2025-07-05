class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and optionally label the emotion.

        The agent's tension increases with the intensity of the new emotion.
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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
        """Return a philosophical answer depending on the current state.

        The current emotional label influences the tone of the response.
        """
        prefix = f"({self.emotion_name}) " if self.emotion_name != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

    def integrate(self, other: "Agent") -> None:
        """Integrate another agent's tension and emotion into this agent."""
        self.tension = (self.tension + other.tension) / 2
        self.emotion = (self.emotion + other.emotion) / 2

    def duplicate(self, suffix: str = "_copy") -> "Agent":
        """Return a duplicate of the agent with a modified name."""
        return Agent(
            name=f"{self.name}{suffix}",
            state=self.state,
            tension=self.tension,
            emotion=self.emotion,
            emotion_name=self.emotion_name,
        )

