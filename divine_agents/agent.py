class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent maintains an internal fame score which decays over time and
    influences its interactions. State transitions are governed by emotion and
    tension levels as described in the ontological specification.
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

    def update_fame(self, positive_actions: int, negative_actions: int,
                    participation_score: float) -> float:
        """Update fame based on actions and apply decay."""
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
        return self.fame

    def apply_fame_decay(self) -> None:
        """Gradually reduce fame over time."""
        if self.fame > 0:
            self.fame -= self.fame * self.decay_rate
            if self.fame < 0:
                self.fame = 0

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

    def fame_tier(self) -> str:
        """Return textual representation of fame tier."""
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
