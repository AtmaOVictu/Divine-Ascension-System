"""Core agent logic for the ontological dialogue system."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent used in dialogues.
    state:
        Ontological state of the agent (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Numerical representation of internal tension ``[0, 1]``.
    emotion:
        Numerical representation of emotional intensity ``[0, 1]``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and update tension.

        Parameters
        ----------
        value:
            New emotional intensity. Values are clamped between ``0`` and ``1``.
        """
        self.emotion = max(0.0, min(value, 1.0))
        self.tension = max(0.0, min(self.tension + self.emotion, 1.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamped to ``[0, 1]``."""
        self.tension = max(0.0, min(value, 1.0))

    def transition(self) -> str:
        """Transition ontological state if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer affected by current emotion and state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            tone = "Z intenzivnim čustvom"
        elif self.emotion > 0.3:
            tone = "Čustveno"
        else:
            tone = "Mirno"
        return f"{tone} povem: {base}"
