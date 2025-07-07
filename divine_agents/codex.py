from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class Codex:
    """Manage interactions and evolution of ontological agents."""

    def __init__(self) -> None:
        self.elements: Dict[str, Agent] = {}

    def add_element(self, element: Agent) -> None:
        """Register a new agent in the codex."""
        self.elements[element.name] = element

    def simulate_interaction(self, agent1: Agent, agent2: Agent) -> List[str]:
        """Simulate a dialogue and trigger potential state transitions."""
        lines: List[str] = []
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # introduce emotion and tension changes
        agent1.update_emotion(0.8)
        agent2.update_emotion(0.6)

        agent1.transition()
        agent2.transition()

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        return lines
