class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks emotional intensity, tension, ontological state and
    fame, which accumulates based on positive actions, negative actions and
    algorithmic participation.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        fame: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = fame
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_fame(
        self, positive: float, negative: float, participation: float
    ) -> float:
        """Update fame according to actions and participation."""
        positive_weight = 1.0
        negative_weight = 1.0
        participation_weight = 1.0

        fame_change = (
            positive * positive_weight
            - negative * negative_weight
            + participation * participation_weight
        )
        self.fame += fame_change
        return self.fame

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
