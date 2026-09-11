class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent also maintains a fame score that is normalised between 0 and 1
    (representing a percentage) together with algorithmic participation. Fame
    decays over time if the agent does not perform positive actions.
    """

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
        self.fame = fame
        self.participation = participation
        self.decay_rate = 0.05  # 5 % fame decay
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Fame system
    # ------------------------------------------------------------------

    def update_fame(
        self,
        positive_actions: float,
        negative_actions: float,
        participation_score: float,
    ) -> float:
        """Update fame based on weighted actions and participation.

        All inputs are expected to be normalised percentages between 0 and 1.
        Fame change is clamped to stay within the same range.
        """
        positive_weight = 0.1
        negative_weight = 0.05
        participation_weight = 0.1

        fame_change = (
            positive_actions * positive_weight
            - negative_actions * negative_weight
            + participation_score * participation_weight
        )
        self.fame += fame_change
        self.fame = min(1.0, max(0.0, self.fame))
        self.apply_fame_decay()
        return self.fame

    def apply_fame_decay(self) -> None:
        """Apply a proportional fame decay."""
        if self.fame > 0.0:
            self.fame -= self.fame * self.decay_rate
            self.fame = max(0.0, self.fame)

    def update_participation(self, new_score: float) -> float:
        """Update algorithmic participation."""
        self.participation = min(1.0, max(0.0, new_score))
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


def fame_tiers(agent: Agent) -> str:
    """Return a fame tier based on fame percentage."""
    if agent.fame <= 0.2:
        return "Unknown"
    if agent.fame <= 0.5:
        return "Moderate Fame"
    if agent.fame <= 0.8:
        return "Influential"
    return "Legendary"


def social_influence(agent: Agent, target_agent: Agent) -> bool:
    """Determine if ``agent`` can influence ``target_agent`` based on fame."""
    fame_influence = (agent.fame - target_agent.fame) * 100
    if fame_influence > 0:
        return True
    return False
