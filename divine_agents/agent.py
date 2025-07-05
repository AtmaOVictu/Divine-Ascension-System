from .companions import ShadowAgent, AngelAgent


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial tension level in range ``0`` to ``1``.
    emotion:
        Initial emotion level in range ``0`` to ``1``.
    shadow:
        Optional :class:`ShadowAgent` influencing this agent.
    angel:
        Optional :class:`AngelAgent` influencing this agent.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: ShadowAgent | None = None,
        angel: AngelAgent | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.shadow = shadow or ShadowAgent()
        self.angel = angel or AngelAgent()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def interact_with_shadow(self) -> str:
        """Invoke the shadow agent's influence."""
        return self.shadow.interact(self)

    def interact_with_angel(self) -> str:
        """Invoke the angel agent's influence."""
        return self.angel.interact(self)

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
