import math


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent maintains an ontological ``state`` (``Ego``, ``Jaz`` or
    ``Enotnost``) along with numeric ``tension`` and ``emotion`` values.
    Transitions occur automatically when ``tension`` exceeds ``0.7`` or
    ``emotion`` exceeds ``0.5``.  ``tension`` slowly decays over time and can
    also be influenced by other agents via :py:meth:`influence`.
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

    def decay_tension(self, time_step: float = 1.0) -> None:
        """Reduce tension gradually based on a simple exponential decay."""
        self.tension *= math.exp(-0.3 * time_step)

    def influence(self, other: "Agent") -> None:
        """Influence another agent's tension based on current emotion."""
        if self.emotion > 0.5:
            other.tension += self.emotion * 0.5
        else:
            other.tension = max(0.0, other.tension - 0.1)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
