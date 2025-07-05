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


class ReflectiveAgent(Agent):
    """Agent that performs self-reflection before transitioning."""

    def self_reflect(self) -> bool:
        """Return True if reflection indicates a state change is needed."""
        if len(self.history) > 1 and self.state == "Enotnost" and self.emotion > 0.7:
            # High emotion while in unity prompts a return to the previous state
            return True
        return False

    def transition(self) -> str:
        """Perform transition considering self-reflection."""
        if self.self_reflect():
            # return to previous state for balance
            self.state = self.history[-2]
            self.history.append(self.state)
        else:
            result = super().transition()
            return result
        return self.state
