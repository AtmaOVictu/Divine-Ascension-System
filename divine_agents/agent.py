class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
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
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if self.state != previous:
            self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class BasicAgent(Agent):
    """Agent operating with simple transition logic."""

    def evolve(self) -> None:
        if self.tension > 0.7:
            self.transition()
        self.update_emotion(min(self.emotion + 0.1, 1.0))


class IntermediateAgent(BasicAgent):
    """Agent that reflects on past actions."""

    def evolve(self) -> None:
        self.tension += 0.2
        super().evolve()


class MasterAgent(IntermediateAgent):
    """Agent guiding others with wisdom."""

    def evolve(self) -> None:
        self.tension += 0.3
        super().evolve()

    def mentor(self, other: Agent) -> None:
        other.update_emotion(other.emotion + 0.1)


class HighMasterAgent(MasterAgent):
    """Highly evolved agent controlling emotional balance."""

    def evolve(self) -> None:
        self.tension += 0.4
        super().evolve()


class GodLikeAgent(HighMasterAgent):
    """Agent capable of shaping the system."""

    def evolve(self) -> None:
        self.tension += 0.5
        super().evolve()

    def create_reality(self) -> str:
        return f"{self.name} shapes new realities."
