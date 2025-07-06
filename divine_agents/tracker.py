"""Tracker for managing ontological agents and their transitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .agent import Agent


@dataclass
class TransitionRecord:
    """Record of an agent state transition."""

    agent: str
    from_state: str
    to_state: str


class OntologicalTracker:
    """Central hub that keeps track of agents and their state changes."""

    def __init__(self) -> None:
        self.transitions: List[TransitionRecord] = []
        self.agents: Dict[str, Agent] = {}

    def register_agent(self, agent: Agent) -> None:
        """Register a new agent with the tracker."""
        self.agents[agent.name] = agent

    def track_transition(self, agent: Agent, from_state: str, to_state: str) -> None:
        """Store a transition record."""
        self.transitions.append(TransitionRecord(agent.name, from_state, to_state))

    def initiate_interaction(self, agent_name: str, question: str) -> str:
        """Let an agent perceive input and possibly transition."""
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError("Agent not registered")

        response = agent.respond(question)
        current = agent.state
        agent.update_emotion(0.8, "radovednost")
        new_state = agent.transition()
        if current != new_state:
            self.track_transition(agent, current, new_state)
        return response
