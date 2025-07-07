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
        """Return a philosophical answer depending on the current state and emotion."""
        mood = ""
        if self.emotion > 0.7:
            mood = " z močnimi čustvi"
        elif self.emotion > 0.3:
            mood = " mirno"

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base}{mood}"


class WideAgent(Agent):
    """Agent capable of handling multiple dimensions and complex transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.dimensions = {"space": 0, "time": 0, "emotion": 0}

    def update_emotion(self, value: float) -> None:
        super().update_emotion(value)
        self.dimensions["emotion"] = value
        self.transition()


class NarrowAgent(Agent):
    """Specialized agent reacting once a threshold is exceeded."""

    def __init__(self, name: str, state: str = "Ego", threshold: float = 0.5):
        super().__init__(name, state)
        self.threshold = threshold
        self.value = 0.0

    def update_value(self, new_value: float) -> None:
        self.value = new_value
        if self.value > self.threshold:
            self.update_tension(new_value)
            self.transition()
