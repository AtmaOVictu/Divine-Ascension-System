from __future__ import annotations

from .agent import Agent


class SimulationPhase:
    """Represents a phase in the agent simulation."""

    def __init__(self, phase_name: str, moral_dilemma: bool = False):
        self.phase_name = phase_name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> None:
        if self.moral_dilemma:
            self.handle_moral_dilemma(agent)

    def handle_moral_dilemma(self, agent: Agent) -> None:
        if agent.state == "Ego":
            decision = "change" if agent.tension > 0.8 else "continue"
            agent.history.append(f"Moral dilemma decision: {decision}")
