class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks emotional intensity, tension, fame and algorithmic
    participation. Fame and participation allow the system to reason about
    how influential an agent is during collective decision making.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, fame: float = 0.0,
                 participation: float = 0.0) -> None:
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

    # Fame and participation -------------------------------------------------

    def update_fame(self, positive_actions: int, negative_actions: int,
                     participation_score: float) -> float:
        """Update fame using positive/negative actions and participation.

        Fame change is influenced by three factors:
        - ``positive_actions`` increase fame with weight 10
        - ``negative_actions`` decrease fame with weight 5
        - ``participation_score`` (0-100) is multiplied by weight 2
        Returns the new fame score.
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

    def update_participation(self, new_score: float) -> float:
        """Set a new algorithmic participation score."""
        self.participation = new_score
        return self.participation

    def influence_score(self) -> float:
        """Compute overall influence based on fame and participation."""
        return (self.fame + self.participation) / 2

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

