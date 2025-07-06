from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class OntologicalTracker:
    """Nest-like tracker managing multiple agents and their transitions."""

    def __init__(self) -> None:
        self.transitions: List[dict] = []
        self.agents: Dict[str, Agent] = {
            "Mojster očesa": Agent("Mojster očesa", state="Ego"),
            "Mojster ušesa": Agent("Mojster ušesa", state="Jaz"),
            "Mojster čuta": Agent("Mojster čuta", state="Enotnost"),
            "Mojster čutil telesa": Agent("Mojster čutil telesa", state="Ego"),
        }

    def add_agent(self, agent: Agent) -> None:
        """Add a new agent to the tracker."""
        self.agents[agent.name] = agent

    def track_transition(self, name: str, from_state: str, to_state: str) -> None:
        """Record a state transition."""
        self.transitions.append({"agent": name, "from": from_state, "to": to_state})

    def interact(self, agent_name: str, input_data: str, emotion: float) -> str:
        """Interact with the given agent and return its response."""
        if agent_name not in self.agents:
            raise ValueError("Agent not found")
        agent = self.agents[agent_name]
        agent.update_emotion(emotion)
        prev_state = agent.state
        response = agent.respond(input_data)
        new_state = agent.transition()
        if new_state != prev_state:
            self.track_transition(agent_name, prev_state, new_state)
        return response
