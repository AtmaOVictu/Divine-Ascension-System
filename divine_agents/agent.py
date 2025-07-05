class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    _id_counter = 1

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        agent_id: int | None = None,
    ) -> None:
        self.name = name
        self.agent_id = agent_id or Agent._id_counter
        Agent._id_counter = max(Agent._id_counter, self.agent_id + 1)
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def __repr__(self) -> str:
        return f"Agent(id={self.agent_id}, name={self.name}, state={self.state})"

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def speak(self, question: str) -> str:
        """Return an emotional response regarding the question."""
        base = self.respond(question)
        if self.emotion > 0.7:
            mood = "z močnim čustvom"
        elif self.emotion > 0.3:
            mood = "z umirjenimi čustvi"
        else:
            mood = "mirno"
        return f"{base} ({mood})"
