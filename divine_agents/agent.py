"""Core logic for ontological agents and their transitions."""

from __future__ import annotations

from dataclasses import dataclass


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp ``value`` between ``minimum`` and ``maximum``."""
    return max(minimum, min(maximum, value))


class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: "ShadowAspect | None" = None,
        angel: "AngelAspect | None" = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = _clamp(tension)
        self.emotion = _clamp(emotion)
        self.shadow = shadow if shadow is not None else ShadowAspect()
        self.angel = angel if angel is not None else AngelAspect()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension with clamping."""
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

    # --- Aspect interaction -------------------------------------------------

    def contact_shadow(self) -> str:
        """Interact with the agent's shadow aspect."""
        return self.shadow.guide(self)

    def contact_angel(self) -> str:
        """Interact with the agent's angelic aspect."""
        return self.angel.guide(self)


@dataclass
class ShadowAspect:
    """Represents the darker aspect of an agent."""

    name: str = "Shadow"

    def guide(self, agent: Agent) -> str:
        agent.update_tension(_clamp(agent.tension + 0.3))
        return f"{agent.name} se soo\u010da s senco {self.name}."


@dataclass
class AngelAspect:
    """Represents the enlightened aspect of an agent."""

    name: str = "Angel"

    def guide(self, agent: Agent) -> str:
        agent.update_emotion(_clamp(agent.emotion + 0.3))
        return f"{agent.name} ga vodi angel {self.name}."
