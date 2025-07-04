class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Display name of the agent.
    state: str
        Current ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension: float
        Accumulated tension that may trigger state transitions.
    emotion: float
        Current emotional intensity in range ``0`` to ``1``.
    history: list[str]
        Historical record of visited states.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension.

        The emotion value is stored directly while also increasing the
        accumulated tension. This models how stronger emotions can lead to
        greater internal pressure.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim intenzivnost {self.emotion:.1f}."
        return base

    def speak(self, question: str) -> str:
        """Return a formatted line representing the agent's answer."""
        reply = self.respond(question)
        return f"{self.name} ({self.state}): {reply}"
