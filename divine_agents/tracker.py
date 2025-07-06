from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class MasterEye(Agent):
    """Agent representing perception through sight."""

    def perceive(self, input_data: str) -> str:
        return f"{self.name} zaznava skozi vid: {input_data}"


class MasterEar(Agent):
    """Agent representing perception through hearing."""

    def perceive(self, input_data: str) -> str:
        return f"{self.name} zaznava skozi sluh: {input_data}"


class MasterSense(Agent):
    """Agent representing a deeper intuitive sense."""

    def perceive(self, input_data: str) -> str:
        return f"{self.name} zaznava skozi čut: {input_data}"


class MasterBodySense(Agent):
    """Agent representing bodily sensations."""

    def perceive(self, input_data: str) -> str:
        return f"{self.name} zaznava telo: {input_data}"


class OntologicalTracker:
    """Central tracker holding all agents and logging transitions."""

    def __init__(self) -> None:
        self.transitions: List[Dict[str, str]] = []
        self.emotional_states: Dict[str, List[float]] = {}
        self.philosophical_debates: Dict[str, List[str]] = {}
        self.agents: Dict[str, Agent] = {
            "Mojster očesa": MasterEye("Mojster očesa"),
            "Mojster ušesa": MasterEar("Mojster ušesa", state="Jaz"),
            "Mojster čuta": MasterSense("Mojster čuta", state="Enotnost"),
            "Mojster čutil telesa": MasterBodySense("Mojster čutil telesa"),
        }

    def track_transition(self, agent_name: str, from_state: str, to_state: str) -> None:
        self.transitions.append({"agent": agent_name, "from": from_state, "to": to_state})

    def track_emotional_change(self, agent_name: str, emotional_state: float) -> None:
        self.emotional_states.setdefault(agent_name, []).append(emotional_state)

    def track_philosophical_debate(self, agent_name: str, debate_topic: str) -> None:
        self.philosophical_debates.setdefault(agent_name, []).append(debate_topic)

    def trigger_transition(self, agent_name: str, current_state: str) -> str:
        agent = self.agents[agent_name]
        new_state = agent.transition()
        if new_state != current_state:
            self.track_transition(agent_name, current_state, new_state)
        return new_state

    def initiate_interaction(self, agent_name: str, input_data: str, emotion: float) -> str:
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError("Agent not found")
        agent.update_emotion(emotion)
        perception = agent.perceive(input_data)
        prev_state = agent.history[-1] if len(agent.history) == 1 else agent.history[-2]
        new_state = self.trigger_transition(agent_name, prev_state)
        return f"{perception} -> {agent.state}"
