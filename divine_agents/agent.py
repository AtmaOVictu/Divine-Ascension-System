class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks fame based on positive/negative actions and participation
    in system algorithms.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        # Fame and participation tracking
        self.positive_actions = 0
        self.negative_actions = 0
        self.algorithm_participation = 0.0
        self.fame = 0.0

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Fame and participation utilities
    def record_action(self, positive: bool) -> None:
        """Record an action and update fame accordingly."""
        if positive:
            self.positive_actions += 1
        else:
            self.negative_actions += 1
        self.recalculate_fame()

    def participate(self, score: float) -> None:
        """Participate in an algorithmic process and increase fame."""
        self.algorithm_participation += score
        self.recalculate_fame()

    def recalculate_fame(self) -> float:
        """Compute fame using positive/negative actions and participation."""
        self.fame = max(
            0.0,
            min(1.0, self.positive_actions * 0.1 - self.negative_actions * 0.1 + self.algorithm_participation),
        )
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
