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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class AgentWithHistory(Agent):
    """Agent that keeps a detailed transition history."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.history = [
            {"state": state, "emotion": emotion, "tension": tension}
        ]

    def update_history(self) -> None:
        """Append the current state snapshot to history."""
        self.history.append(
            {"state": self.state, "emotion": self.emotion, "tension": self.tension}
        )

    def transition(self) -> str:
        """Transition with consideration of recent history."""
        if len(self.history) >= 3:
            avg_tension = sum(h["tension"] for h in self.history[-3:]) / 3
            if avg_tension > 0.6 and self.state == "Ego":
                self.state = "Jaz"
            elif avg_tension > 0.5 and self.state == "Jaz":
                self.state = "Enotnost"

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        self.update_history()
        return self.state


class EmotionalAgent(Agent):
    """Agent capable of influencing another agent emotionally."""

    def interact(self, other_agent: "Agent") -> None:
        if self.state != other_agent.state:
            mutual_influence = min(self.tension, other_agent.tension) * 0.1
            self.update_emotion(self.emotion + mutual_influence)
            other_agent.update_emotion(other_agent.emotion + mutual_influence)
