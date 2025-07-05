class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.love = 0.0
        self.hate = 0.0
        self.history = [state]
        self.philosophical_context = {}

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_love(self, value: float) -> None:
        """Update love level and recalculate emotion."""
        self.love = value
        self.update_emotion(self.love - self.hate)

    def update_hate(self, value: float) -> None:
        """Update hate level and recalculate emotion."""
        self.hate = value
        self.update_emotion(self.love - self.hate)

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

    def philosophical_analysis(self) -> None:
        """Assign a philosophical description based on emotional balance."""
        if self.love > self.hate:
            msg = "Agent is following a path of love and unity."
        elif self.hate > self.love:
            msg = "Agent is experiencing conflict and division."
        else:
            msg = "Agent is in a state of equilibrium."
        self.philosophical_context[self.name] = msg

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
