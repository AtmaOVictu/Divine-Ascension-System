class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = 0.0
        self.participation = 0.0
        self.decay_rate = 0.05
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

    # --- Fame management -------------------------------------------------

    def update_fame(self, positive_actions: float, negative_actions: float, participation_score: float) -> float:
        """Update fame based on actions and participation (values 0-1)."""
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
        """Reduce fame proportionally based on decay rate."""
        if self.fame > 0.0:
            self.fame -= self.fame * self.decay_rate
            self.fame = max(0.0, self.fame)

    def update_participation(self, new_participation_score: float) -> float:
        """Set the agent's algorithmic participation within 0 and 1."""
        self.participation = min(1.0, max(0.0, new_participation_score))
        return self.participation


def fame_tiers(agent: Agent) -> str:
    """Return fame tier based on the agent's fame percentage."""
    if agent.fame <= 0.2:
        return "Unknown"
    elif agent.fame <= 0.5:
        return "Moderate Fame"
    elif agent.fame <= 0.8:
        return "Influential"
    return "Legendary"


def social_influence(agent: Agent, target_agent: Agent) -> bool:
    """Determine whether one agent can influence another based on fame."""
    fame_influence = (agent.fame - target_agent.fame) * 100
    if fame_influence > 0:
        return True
    return False
