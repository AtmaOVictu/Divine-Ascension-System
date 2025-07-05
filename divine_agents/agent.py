"""Core agent module."""

from typing import Optional


def _clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    """Clamp a floating point value between ``min_value`` and ``max_value``."""
    return max(min_value, min(max_value, value))


class AngelAgent:
    """Light aspect guiding the main agent towards higher principles."""

    def __init__(self, name: str):
        self.name = name

    def guide(self) -> str:
        """Return a short inspirational message."""
        return f"{self.name} vodi te k svetlobi."


class ShadowAgent:
    """Shadow aspect representing the darker impulses of the main agent."""

    def __init__(self, name: str):
        self.name = name

    def whisper(self) -> str:
        """Return a tempting whisper from the shadows."""
        return f"{self.name} vabi te v temo."


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial tension level. Values are clamped between 0 and 1.
    emotion:
        Initial emotion level. Values are clamped between 0 and 1.
    angel:
        Optional :class:`AngelAgent` connection.
    shadow:
        Optional :class:`ShadowAgent` connection.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        angel: Optional[AngelAgent] | None = None,
        shadow: Optional[ShadowAgent] | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = _clamp(tension)
        self.emotion = _clamp(emotion)
        self.angel = angel
        self.shadow = shadow
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion by ``value`` and clamp both emotion and tension."""
        self.emotion = _clamp(self.emotion + value)
        self.tension = _clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level (clamped)."""
        self.tension = _clamp(value)

    def transition(self) -> str:
        """Transition to the next ontological state if thresholds are exceeded."""
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
