class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent also tracks ``fame`` and ``participation`` which are expressed
    as percentages between ``0.0`` and ``1.0``. Fame may decay over time and
    influences social interactions.
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
        decay_rate: float = 0.05,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = fame
        self.participation = participation
        self.decay_rate = decay_rate
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    # Fame system -----------------------------------------------------------

    def update_fame(
        self,
        positive_actions: float,
        negative_actions: float,
        participation_score: float,
    ) -> float:
        """Update fame based on actions and participation.

        All inputs are expected to be in the range ``0.0`` to ``1.0``.
        Fame is clamped between ``0.0`` and ``1.0`` after the update and
        may then be reduced by decay.
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
        self.fame = max(0.0, min(1.0, self.fame))
        self.apply_fame_decay()
        return self.fame

    def apply_fame_decay(self) -> None:
        """Apply fame decay proportional to the current fame."""
        if self.fame > 0.0:
            self.fame -= self.fame * self.decay_rate
            self.fame = max(0.0, self.fame)

    def update_participation(self, new_participation_score: float) -> float:
        """Update algorithmic participation."""
        self.participation = max(0.0, min(1.0, new_participation_score))
        return self.participation

    @property
    def fame_tier(self) -> str:
        """Return a fame tier name based on ``self.fame``."""
        if self.fame <= 0.2:
            return "Unknown"
        if self.fame <= 0.5:
            return "Moderate Fame"
        if self.fame <= 0.8:
            return "Influential"
        return "Legendary"

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

def social_influence(agent: "Agent", target_agent: "Agent") -> bool:
    """Return ``True`` if ``agent`` can influence ``target_agent``.

    Influence is calculated from the fame difference expressed as a
    percentage. Agents with higher fame can influence less famous ones.
    """

    fame_diff = (agent.fame - target_agent.fame) * 100
    if fame_diff > 0:
        return True
    return False


def emotional_state(agent: "Agent") -> str:
    """Return a textual emotional state influenced by fame."""
    if agent.fame >= 0.8:
        return "Arrogant or Overconfident"
    if agent.fame >= 0.5:
        return "Balanced and Calm"
    if agent.fame >= 0.2:
        return "Insecure and Eager"
    return "Frustrated or Isolated"
