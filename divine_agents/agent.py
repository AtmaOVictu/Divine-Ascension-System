class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or {"anger": 0.0, "joy": 0.0, "fear": 0.0}
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update a specific emotion and recalculate tension."""
        if emotion_type in self.emotion:
            self.emotion[emotion_type] = value
        self.calculate_tension()

    def calculate_tension(self) -> None:
        """Recalculate tension based on the current emotional state."""
        self.tension = sum(self.emotion.values()) / len(self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or any(e > 0.5 for e in self.emotion.values()):
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
    """Agent that keeps detailed transition history to influence future states."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: dict | None = None, history: list | None = None):
        super().__init__(name, state, tension, emotion)
        self.full_history: list[dict] = history or []

    def update_history(self) -> None:
        """Store current state snapshot in history."""
        self.full_history.append({
            "state": self.state,
            "emotion": self.emotion.copy(),
            "tension": self.tension,
        })

    def transition(self) -> str:
        """Transition using history-aware logic then call base transition."""
        if len(self.full_history) > 3:
            avg_tension = sum(h["tension"] for h in self.full_history[-3:]) / 3
            if avg_tension > 0.6:
                self.state = "Jaz"
            elif avg_tension > 0.5:
                self.state = "Enotnost"
        new_state = super().transition()
        self.update_history()
        return new_state


class EmotionalAgent(Agent):
    """Agent supporting emotional interactions with other agents."""

    def interact(self, other: "EmotionalAgent") -> None:
        """Modify tension and emotions based on interaction with another agent."""
        if self.state != other.state:
            mutual_influence = min(self.tension, other.tension) * 0.1
            self.tension += mutual_influence
            other.tension += mutual_influence
            self.update_emotion("anger", self.emotion["anger"] + mutual_influence)
            other.update_emotion("fear", other.emotion["fear"] + mutual_influence)
