class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Starting ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        """
        if state not in self.STATES:
            raise ValueError(f"Unknown state: {state}")
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update the emotional level and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the current tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            prefix = "Z veliko strastjo: "
        elif self.emotion > 0.4:
            prefix = "Mirno: "
        else:
            prefix = "Nevtralno: "
        return prefix + base
