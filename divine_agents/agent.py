"""Agent implementation for the Divine-Ascension-System."""

from __future__ import annotations

from dataclasses import dataclass


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp ``value`` to the inclusive range [minimum, maximum]."""
    return max(minimum, min(maximum, value))


class ShadowAgent:
    """Represents the darker companion influencing an :class:`Agent`."""

    def __init__(self, name: str):
        self.name = name

    def influence(self, agent: "Agent") -> None:
        """Increase the agent's tension slightly."""
        agent.update_tension(agent.tension + 0.2)


class AngelAgent:
    """Represents the guiding companion helping an :class:`Agent`."""

    def __init__(self, name: str):
        self.name = name

    def influence(self, agent: "Agent") -> None:
        """Decrease the agent's tension slightly."""
        agent.update_tension(agent.tension - 0.2)


class Agent:
    """Ontological agent capable of transitioning between philosophical states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Starting ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial tension level. Value will be clamped to the range ``[0, 1]``.
    emotion:
        Initial emotion intensity. Value will be clamped to ``[0, 1]``.
    shadow:
        Optional :class:`ShadowAgent` companion.
    angel:
        Optional :class:`AngelAgent` companion.
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
        self.tension = _clamp(tension)
        self.emotion = _clamp(emotion)
        self.shadow = shadow
        self.angel = angel
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion by ``value`` and clamp both emotion and tension.

        Parameters
        ----------
        value:
            Amount by which the current emotional intensity should change.
        """
        self.emotion = _clamp(self.emotion + value)
        self.tension = _clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Set tension level to ``value`` while clamping the result."""
        self.tension = _clamp(value)

    def transition(self) -> str:
        """Perform a state transition if tension or emotion exceed thresholds."""
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

    def contact_shadow(self) -> None:
        """Connect with the shadow companion if present."""
        if self.shadow:
            self.shadow.influence(self)

    def contact_angel(self) -> None:
        """Connect with the angel companion if present."""
        if self.angel:
            self.angel.influence(self)
