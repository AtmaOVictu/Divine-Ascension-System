class Agent:
    """Represents an ontological agent capable of transitioning states.

    Legitimate transitions occur only when the agent's tension or emotion
    exceeds predefined thresholds. If a transition is forced without meeting
    these thresholds it is considered an "amateur" transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def is_legitimate_transition(self) -> bool:
        """Return True if thresholds for a legitimate transition are met."""
        return self.tension > 0.7 or self.emotion > 0.5

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self, force: bool = False) -> str:
        """Perform a state transition.

        By default the transition only occurs when legitimate thresholds are
        exceeded. When ``force`` is ``True`` the transition occurs regardless,
        representing an amateur or compelled change.
        """
        if self.is_legitimate_transition() or force:
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
