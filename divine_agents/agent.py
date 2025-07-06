class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        team=None,
        loyalty: float = 0.5,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.team = team or []
        self.loyalty = loyalty
        self.history = [state]
        self.decisions_history = []

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

    def make_moral_decision(self, situation: str) -> str:
        """Determine a decision based on emotion and loyalty."""
        if self.emotional_state == "fearful":
            decision = f"{self.name} chooses self-preservation in {situation}."
        elif self.emotional_state == "happy" and self.loyalty > 0.7:
            decision = f"{self.name} decides to help others selflessly in {situation}."
        elif self.loyalty <= 0.5:
            decision = f"{self.name} prioritizes personal gain in {situation}."
        else:
            decision = f"{self.name} hesitates in {situation} due to internal conflict."
        self.decisions_history.append(decision)
        return decision

    def team_decision(self) -> None:
        """Influence team members by encouraging risk avoidance."""
        if not self.team:
            return
        for member in self.team:
            if member is self:
                continue
            decision = f"{member.name} avoids risk due to group decision."
            member.decisions_history.append(decision)
