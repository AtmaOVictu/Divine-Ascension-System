class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent also maintains a ``fame`` metric that influences its social
    standing within the system. Fame can increase or decrease based on
    interactions and decays over time if not maintained.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, fame: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = fame
        self.decay_rate = 0.05
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Fame -----------------------------------------------------------------
    def update_fame(self, positive_actions: int = 0, negative_actions: int = 0,
                    participation_score: float = 0.0) -> float:
        """Update fame based on interactions and apply decay.

        Fame increases with positive actions and participation but decreases
        with negative actions. After applying the change the fame decay for
        this cycle is also applied.
        """
        positive_weight = 10
        negative_weight = 5
        participation_weight = 2

        fame_change = (
            positive_actions * positive_weight
            - negative_actions * negative_weight
            + participation_score * participation_weight
        )
        self.fame += fame_change
        self.apply_fame_decay()
        # Fame cannot be negative
        if self.fame < 0:
            self.fame = 0
        return self.fame

    def apply_fame_decay(self) -> None:
        """Apply decay to fame if above zero."""
        if self.fame > 0:
            self.fame -= self.fame * self.decay_rate
            if self.fame < 0:
                self.fame = 0

    # ----------------------------------------------------------------------

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def fame_tier(self) -> str:
        """Return textual fame tier based on current fame value."""
        if self.fame <= 20:
            return "Unknown"
        if self.fame <= 50:
            return "Moderate Fame"
        if self.fame <= 80:
            return "Influential"
        return "Legendary"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
