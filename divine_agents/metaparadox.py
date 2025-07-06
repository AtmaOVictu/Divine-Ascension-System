"""System-level constructs for metaparadox analysis."""

from .agent import Agent


class MetaAgent:
    """Wraps an :class:`Agent` and tracks metaparadox transitions."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.activities = []

    def analyze_transition(self) -> str:
        """Perform a transition and log the metaparadox message."""
        new_state = self.agent.transition()
        message = (
            f"Metaparadoks: agent {self.agent.name} je prešel v {new_state}, "
            "vendar prehod odpira novo vprašanje."
        )
        self.activities.append(message)
        return message


class FilozofskiPrehod:
    """Map agent states to philosophical truths."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def prehod_resnice(self) -> str:
        """Return the philosophical truth for the agent's state."""
        if self.agent.state == "Ego":
            return "Absolutna resnica"
        if self.agent.state == "Jaz":
            return "Relativna resnica"
        if self.agent.state == "Enotnost":
            return "Enotna resnica"
        return "Neznana resnica"

