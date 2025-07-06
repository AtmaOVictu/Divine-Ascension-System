class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
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

    def make_moral_decision(self, situation: str) -> str:
        """Decide morally based on emotion and loyalty."""
        if self.emotion > 0.6 and self.loyalty < 0.5:
            decision = f"{self.name} prioritizes self-preservation in {situation}."
        elif self.loyalty > 0.7:
            decision = f"{self.name} helps others selflessly in {situation}."
        else:
            decision = f"{self.name} decides to act in their own interest in {situation}."
        self.history.append(decision)
        return decision


def team_decision(team: list[Agent]) -> str:
    """Make a simple decision for the team based on emotions."""
    emotions = [member.emotion for member in team]
    if sum(e > 0.6 for e in emotions) > len(team) / 2:
        return "Team takes a risk with optimism!"
    if sum(e < -0.5 for e in emotions) > len(team) / 2:
        return "Team avoids risk due to fear."
    return "Team makes a neutral decision."
