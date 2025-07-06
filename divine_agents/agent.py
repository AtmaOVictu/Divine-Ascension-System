class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent keeps track of emotional state, tension, and all decisions made so
    that meta tests can verify every possible branch of execution.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_state: str = "neutral",
        team: list | None = None,
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state
        self.team = team or []
        self.loyalty = loyalty
        self.history = [state]
        self.decisions_history: list[str] = []

    def update_emotion(self, value: float, emotion_state: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_state is not None:
            self.emotion_state = emotion_state
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

    def make_moral_decision(self, situation: str) -> str:
        """Return a decision string based on emotion and loyalty."""
        if self.emotion_state == "fear":
            decision = f"{self.name} chooses self-preservation in {situation}."
        elif self.emotion_state == "joy" and self.loyalty > 0.7:
            decision = f"{self.name} decides to help others selflessly in {situation}."
        elif self.loyalty <= 0.5:
            decision = f"{self.name} prioritizes personal gain in {situation}."
        else:
            decision = f"{self.name} hesitates in {situation} due to internal conflict."
        self.decisions_history.append(decision)
        return decision

    def team_decision(self) -> str:
        """Make a decision influenced by team tension."""
        if not self.team:
            return ""
        avg_tension = sum(member.tension for member in self.team) / len(self.team)
        if avg_tension > 0.5:
            decision = "avoids risk"
        else:
            decision = "takes action"
        for member in self.team:
            member.decisions_history.append(f"{member.name} {decision} due to team dynamic.")
        return decision

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
