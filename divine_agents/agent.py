class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks emotional intensity, tension, fame and participation.
    State transitions occur when either ``tension`` is greater than 0.7 or
    ``emotion`` is greater than 0.5. Fame represents how influential the agent
    is within the system and can be increased through positive actions and
    participation in collective decisions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, fame: int = 0, participation: int = 0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = fame
        self.participation = participation
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Fame and participation handling
    def update_fame(self, positive_actions: int, negative_actions: int,
                    participation_score: int) -> int:
        """Update fame based on actions and participation.

        ``positive_actions`` increases fame with weight 10, ``negative_actions``
        decreases fame with weight 5 and ``participation_score`` is multiplied
        by 2.
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
        return self.fame

    def update_participation(self, score: int) -> int:
        """Set the participation score."""
        self.participation = score
        return self.participation

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
