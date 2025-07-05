from __future__ import annotations

from typing import List, Optional


class Agent:
    """Ontological agent capable of transitioning between philosophical states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Starting tension level clamped to ``0``..``1``.
    emotion:
        Starting emotion level clamped to ``0``..``1``.
    shadow_agent:
        Optional reference to the agent's shadow aspect.
    angel_agent:
        Optional reference to the agent's angelic aspect.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow_agent: Optional[Agent] = None,
        angel_agent: Optional[Agent] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.history: List[str] = [state]
        self.shadow_agent = shadow_agent
        self.angel_agent = angel_agent

    @staticmethod
    def _clamp(value: float) -> float:
        """Return ``value`` limited to the ``0``..``1`` range."""
        if value < 0.0:
            return 0.0
        if value > 1.0:
            return 1.0
        return value

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        The resulting values are clamped between ``0`` and ``1`` to
        prevent runaway growth.
        """
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level with clamping."""
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Transition to a higher state if emotion or tension exceed thresholds."""
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
