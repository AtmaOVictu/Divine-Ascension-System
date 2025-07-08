from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - for typing only
    from .agent import Agent


class Environment:
    """Represents external conditions influencing agents."""

    def __init__(self, pressure: float = 0.0):
        self.pressure = pressure

    def influence(self, agent: "Agent") -> None:
        """Modify an agent's tension based on environmental pressure."""
        new_tension = min(1.0, agent.tension + self.pressure)
        agent.update_tension(new_tension)
