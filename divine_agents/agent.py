"""Core agent logic used by the Divine Ascension system."""

from dataclasses import dataclass
from typing import Optional


def _clamp(value: float) -> float:
    """Clamp a numeric value between 0 and 1."""
    return max(0.0, min(1.0, value))


@dataclass
class ShadowAgent:
    """Represents the agent's shadow aspect."""

    name: str = "Shadow"

    def reflect(self) -> str:
        return "Soočam se s svojo temno platjo."


@dataclass
class AngelAgent:
    """Represents the agent's angelic aspect."""

    name: str = "Angel"

    def guide(self) -> str:
        return "Sledim svetlemu načelu."


class Agent:
    """Ontological agent capable of transitioning between states.

    Parameters
    ----------
    name:
        Agent's identifier.
    state:
        Starting ontological state, defaults to ``"Ego"``.
    tension:
        Initial tension value which is clamped to the ``[0, 1]`` range.
    emotion:
        Initial emotion value which is clamped to the ``[0, 1]`` range.
    shadow:
        Optional connection to a :class:`ShadowAgent` representing the dark side.
    angel:
        Optional connection to an :class:`AngelAgent` representing the bright side.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: Optional[ShadowAgent] = None,
        angel: Optional[AngelAgent] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = _clamp(tension)
        self.emotion = _clamp(emotion)
        self.history = [state]
        self.shadow = shadow or ShadowAgent()
        self.angel = angel or AngelAgent()

    def update_emotion(self, value: float) -> None:
        """Update emotion value and adjust tension.

        The resulting emotion is clamped to ``[0, 1]``. Increasing emotion
        raises tension by the same amount which is also clamped.
        """

        self.emotion = _clamp(value)
        self.tension = _clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Set tension level ensuring it stays within ``[0, 1]``."""
        self.tension = _clamp(value)

    def transition(self) -> str:
        """Transition to the next ontological state when limits are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state."""
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih. "
                f"(čustvo: {self.emotion:.2f})"
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi. "
                f"(čustvo: {self.emotion:.2f})"
            )
        return (
            "Vse resnice so eno, medsebojno povezane. "
            f"(čustvo: {self.emotion:.2f})"
        )
