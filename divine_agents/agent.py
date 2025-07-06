class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    #: Possible ontological states in their transition order.
    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Display name of the agent.
        state:
            Initial ontological state. Defaults to ``"Ego"``.
        tension:
            Starting tension value.
        emotion:
            Initial emotion intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotional intensity and adjust tension.

        The new emotion value is stored and also contributes directly to
        accumulated tension. Higher emotion increases the likelihood of a
        state transition.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion > 0.7:
            prefix = "Z mocnimi custvi povem: "
        elif self.emotion > 0.3:
            prefix = "Rahlo custveno trdim: "
        else:
            prefix = ""
        return prefix + base
