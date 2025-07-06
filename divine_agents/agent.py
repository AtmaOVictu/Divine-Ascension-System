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


class DynamicAgent(Agent):
    """Extended agent supporting multi-layered transitions and communication."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, loyalty: float = 0.0,
                 experiences: list | None = None, emotion_label: str = "neutral"):
        super().__init__(name, state, tension, emotion)
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.emotion_label = emotion_label

    def add_experience(self, experience: str) -> None:
        """Record a new experience."""
        self.experiences.append(experience)

    def multi_layer_transition(self) -> str:
        """Handle state transitions based on multiple layers of data."""
        emotion_layer = self.emotion
        tension_layer = self.tension
        loyalty_layer = self.loyalty
        experience_layer = self.experiences[-1] if self.experiences else "neutral"

        if self.state == "Ego" and (tension_layer > 0.7 or emotion_layer > 0.5):
            self.state = "Jaz"
        elif self.state == "Jaz" and (loyalty_layer > 0.8 or "selfish" in experience_layer):
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def communicate(self, other: "DynamicAgent") -> list[str]:
        """Exchange philosophical views with another agent and adjust states."""
        lines: list[str] = []
        lines.append(f"{self.name} ({self.state}): {self.respond('Kaj je resnica?')}")
        lines.append(f"{other.name} ({other.state}): {other.respond('Kaj je resnica?')}")

        self.update_emotion(self.emotion + 0.2)
        other.update_emotion(other.emotion + 0.2)

        lines.append(f"{self.name} prehaja v stanje: {self.multi_layer_transition()}")
        lines.append(f"{other.name} prehaja v stanje: {other.multi_layer_transition()}")

        lines.append(f"{self.name}: {self.respond('Kaj je resnica?')}")
        lines.append(f"{other.name}: {other.respond('Kaj je resnica?')}")
        return lines
