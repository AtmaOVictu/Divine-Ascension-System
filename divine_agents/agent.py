"""Ontological agent capable of transitioning states."""

from .legitimator import Legitimator


class Agent:
    """Represents an ontological agent with emotion and tension."""

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

    def update(self, tension: float, emotion: float) -> str:
        """Set tension and emotion then attempt a transition."""
        self.tension = tension
        self.emotion = emotion
        return self.transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self, force: bool = False) -> str:
        """Transition to the next state using :class:`Legitimator`."""
        Legitimator.transition(self, force=force)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
