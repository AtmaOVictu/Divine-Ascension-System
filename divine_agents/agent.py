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


class VersionedAgent(Agent):
    """Agent that can transition through different versions when contacting others."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, version: str = "verzija 1"):
        super().__init__(name, state, tension, emotion)
        self.version = version

    def transition_version(self, new_version: str) -> None:
        """Transition to a different version."""
        self.version = new_version

    def touch(self, other: "Agent") -> None:
        """Handle contact with another agent leading to version change and possible state update."""
        # Increase emotion slightly due to interaction which may raise tension
        self.update_emotion(self.emotion + 0.2)
        if self.state == "Ego" and other.state == "Jaz":
            self.transition_version("verzija 2")
        elif self.state == "Jaz" and other.state == "Enotnost":
            self.transition_version("verzija 3")
        else:
            self.transition_version("verzija 1")
        # After contact, evaluate state transition
        self.transition()

