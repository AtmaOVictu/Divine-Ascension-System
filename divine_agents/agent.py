class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        fame: float = 0.0,
        participation: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        # Fame related attributes expressed as percentages (0.0 - 1.0)
        self.fame = self._clamp(fame)
        self.participation = self._clamp(participation)
        self.decay_rate = 0.05

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp value between 0.0 and 1.0."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_participation(self, new_participation_score: float) -> float:
        """Update the agent's algorithmic participation percentage."""
        self.participation = self._clamp(new_participation_score)
        return self.participation

    def update_fame(
        self,
        positive_actions: float,
        negative_actions: float,
        participation_score: float,
    ) -> float:
        """Update fame using weighted inputs in percentage form."""
        positive_weight = 0.1
        negative_weight = 0.05
        participation_weight = 0.1
        fame_change = (
            positive_actions * positive_weight
            - negative_actions * negative_weight
            + participation_score * participation_weight
        )
        self.fame = self._clamp(self.fame + fame_change)
        self.apply_fame_decay()
        return self.fame

    def apply_fame_decay(self) -> None:
        """Decay fame proportionally to the current fame."""
        if self.fame > 0.0:
            self.fame = self._clamp(self.fame - self.fame * self.decay_rate)

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


def fame_tier(agent: Agent) -> str:
    """Return fame tier label based on the agent's fame percentage."""
    fame = agent.fame
    if fame <= 0.2:
        return "Unknown"
    if fame <= 0.5:
        return "Moderate Fame"
    if fame <= 0.8:
        return "Influential"
    return "Legendary"
