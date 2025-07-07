"""Ontological agents and philosophical state management."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name:
        Human readable name of the agent.
    state:
        Current ontological phase (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Accumulated tension affecting state transitions.
    emotion:
        Emotional intensity influencing transitions.
    history:
        List of previously visited states.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Display name for the agent.
        state:
            Starting ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotional intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension.

        The emotional value influences tension accumulation and is clipped to the
        ``0-1`` range.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level within ``0-1`` bounds."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform a state transition based on tension or emotion thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        tone = " razburjeno" if self.emotion > 0.5 else " mirno"
        return f"{base} ({tone})"
