"""Ontological agents and their state transitions."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current tension level between ``0`` and ``1``.
    emotion:
        Current emotional intensity between ``0`` and ``1``.
    """

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

    def influence(self, other: "Agent") -> None:
        """Modify emotion and tension based on another agent.

        A small portion of the other agent's emotional state and tension
        contributes to this agent's own values, representing emotional
        contagion and interactive influence.
        """
        self.emotion = min(1.0, self.emotion + other.emotion * 0.2)
        self.tension = min(1.0, self.tension + other.tension * 0.1)

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
