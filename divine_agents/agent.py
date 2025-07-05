"""Agent models and utilities for the Divine Ascension system."""

from typing import Optional


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp ``value`` between ``minimum`` and ``maximum``."""
    return max(minimum, min(maximum, value))


class Agent:
    """Ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Starting ontological state (``"Ego"`` by default).
    tension:
        Initial tension value. Values are clamped between 0 and 1.
    emotion:
        Initial emotion intensity. Values are clamped between 0 and 1.
    shadow_agent:
        Optional reference to a :class:`ShadowAgent`.
    angel_agent:
        Optional reference to an :class:`AngelAgent`.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow_agent: Optional["ShadowAgent"] = None,
        angel_agent: Optional["AngelAgent"] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = _clamp(tension)
        self.emotion = _clamp(emotion)
        self.history = [state]
        self.shadow_agent = shadow_agent
        self.angel_agent = angel_agent

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        The resulting emotion and tension values are clamped to stay within
        ``0`` and ``1`` to avoid runaway growth.
        """
        self.emotion = _clamp(value)
        self.tension = _clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level with clamping."""
        self.tension = _clamp(value)

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

    def contact_shadow(self) -> str:
        """Interact with the attached shadow agent if present."""
        if not self.shadow_agent:
            return f"{self.name} nima senčne strani."
        return self.shadow_agent.enter_shadow_dimension(self)

    def contact_angel(self) -> str:
        """Interact with the attached angel agent if present."""
        if not self.angel_agent:
            return f"{self.name} nima angelske strani."
        return self.angel_agent.enter_angel_dimension(self)
