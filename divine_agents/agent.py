class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, version: str = "verzija 1"):
        """Initialize the agent.

        Parameters
        ----------
        name:
            Human readable identifier.
        state:
            Starting ontological state.
        tension:
            Initial tension level. Clamped between ``0`` and ``1``.
        emotion:
            Initial emotion intensity. Clamped between ``0`` and ``1``.
        version:
            Current behavioural version of the agent.
        """

        self.name = name
        self.state = state
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.version = version
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity.

        The resulting emotion value is clamped between ``0`` and ``1`` and the
        same increment is added to tension which is also clamped.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level and clamp it between ``0`` and ``1``."""
        self.tension = max(0.0, min(1.0, value))

    def contact(self, other: "Agent") -> None:
        """Update the agent's version based on interaction with ``other``."""
        if self.state == "Ego" and other.state == "Jaz":
            self.version = "verzija 2"
        elif self.state == "Jaz" and other.state == "Enotnost":
            self.version = "verzija 3"
        else:
            self.version = "verzija 1"

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
        """Return a philosophical answer influenced by emotion and state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return base + " Čutim močna čustva."
        if self.emotion < 0.3:
            return base + " Ostajam miren."
        return base
