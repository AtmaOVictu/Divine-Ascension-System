class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent maintains an ``emotion`` and ``tension`` level which dictate
    when a transition between the ontological phases should occur.  The phases
    are ordered as ``Ego`` -> ``Jaz`` -> ``Enotnost`` and no further transition
    occurs once the final state is reached.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Human readable identifier for the agent.
        state:
            Initial ontological state of the agent.
        tension:
            Initial level of tension.
        emotion:
            Initial level of emotion intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def adjust_emotion(self, delta: float) -> None:
        """Modify the current emotion by ``delta`` and propagate to tension."""
        self.update_emotion(self.emotion + delta)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        when either ``tension`` exceeds ``0.7`` or ``emotion`` exceeds
        ``0.5``.  The current state is appended to ``history`` and returned.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def __repr__(self) -> str:
        return (f"Agent(name={self.name!r}, state={self.state!r}, "
                f"tension={self.tension:.2f}, emotion={self.emotion:.2f})")

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def speak(self, topic: str) -> str:
        """Return a dialogue line reflecting the current emotional state."""
        response = self.respond(topic)
        return f"{response} (čustvo: {self.emotion:.2f}, napetost: {self.tension:.2f})"
