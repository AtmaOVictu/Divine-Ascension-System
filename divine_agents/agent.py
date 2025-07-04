"""Ontological agent module.

This module defines the :class:`Agent` class which models an entity that can
transition between the ontological states *Ego*, *Jaz* and *Enotnost*.  The
transition logic is driven by ``tension`` and ``emotion`` levels which mirror
the philosophical instructions provided in the repository description.
"""

class Agent:
    """Represent an ontological agent capable of transitioning states."""

    # Valid ontological states an agent can occupy.
    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0) -> None:
        """Create a new :class:`Agent`.

        Parameters
        ----------
        name:
            Unique identifier for the agent.
        state:
            Initial ontological state. Defaults to ``"Ego"``.
        tension:
            Initial tension value.
        emotion:
            Initial emotion intensity.
        """

        if state not in self.STATES:
            raise ValueError(f"Invalid state: {state}")

        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = float(value)
        self.tension += self.emotion

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = float(value)

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
        """Return a philosophical statement reflecting state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih"
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi"
        else:
            base = "Vse resnice so eno, medsebojno povezane"

        if self.emotion > 0.7:
            tone = "!"
        elif self.emotion < 0.3:
            tone = "."
        else:
            tone = "..."

        return f"{base}{tone}"
