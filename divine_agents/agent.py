"""Ontological agent definitions."""

from __future__ import annotations

from typing import Optional


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Initial ontological state. One of :data:`STATES`.
    tension:
        Starting tension level; values are clamped to ``[0, 1]``.
    emotion:
        Starting emotion intensity; values are clamped to ``[0, 1]``.
    shadow:
        Optional reference to an agent's shadow aspect.
    angel:
        Optional reference to an agent's angelic aspect.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: Optional["ShadowAgent"] = None,
        angel: Optional["AngelAgent"] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.shadow = shadow
        self.angel = angel
        self.history = [state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp ``value`` to the ``[0, 1]`` interval."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension.

        The new emotion value is clamped to the ``[0, 1]`` range. Tension is
        increased by the same amount and clamped as well.
        """
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamped to ``[0, 1]``."""
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Transition the agent's state if thresholds are exceeded.

        Transition occurs when ``tension`` is above ``0.7`` or ``emotion`` is
        above ``0.5``. ``Ego`` transitions to ``Jaz`` and ``Jaz`` transitions to
        ``Enotnost``. ``Enotnost`` is terminal.
        """
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
