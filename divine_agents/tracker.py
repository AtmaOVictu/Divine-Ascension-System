"""Tracker module to manage ontological agents.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from .agent import Agent


class MasterEye(Agent):
    """Agent perceiving the world through sight."""

    def __init__(self) -> None:
        super().__init__("Mojster očesa", state="Ego")

    def perceive(self, input_data: str) -> str:
        return f"Vidim {input_data}"


class MasterEar(Agent):
    """Agent perceiving the world through hearing."""

    def __init__(self) -> None:
        super().__init__("Mojster ušesa", state="Jaz")

    def perceive(self, input_data: str) -> str:
        return f"Slišim {input_data}"


class MasterSense(Agent):
    """Agent perceiving subtle sensations."""

    def __init__(self) -> None:
        super().__init__("Mojster čuta", state="Enotnost")

    def perceive(self, input_data: str) -> str:
        return f"Čutim {input_data}"


class MasterBodySense(Agent):
    """Agent aware of bodily sensations."""

    def __init__(self) -> None:
        super().__init__("Mojster čutil telesa", state="Ego")

    def perceive(self, input_data: str) -> str:
        return f"Zaznavam {input_data} v telesu"


class OntologicalTracker:
    """Nest for managing agents and tracking their interactions."""

    def __init__(self) -> None:
        self.transitions: List[Dict[str, str]] = []
        self.emotional_states: Dict[str, List[float]] = {}
        self.philosophical_debates: Dict[str, List[str]] = {}
        self.agents: Dict[str, Agent] = {
            "Mojster očesa": MasterEye(),
            "Mojster ušesa": MasterEar(),
            "Mojster čuta": MasterSense(),
            "Mojster čutil telesa": MasterBodySense(),
        }

    def track_transition(self, agent_name: str, from_state: str, to_state: str) -> None:
        self.transitions.append({"agent": agent_name, "from": from_state, "to": to_state})

    def track_emotional_change(self, agent_name: str, emotional_state: float) -> None:
        self.emotional_states.setdefault(agent_name, []).append(emotional_state)

    def track_philosophical_debate(self, agent_name: str, debate_topic: str) -> None:
        self.philosophical_debates.setdefault(agent_name, []).append(debate_topic)

    def trigger_transition(self, agent: Agent) -> None:
        previous = agent.state
        new_state = agent.transition()
        if previous != new_state:
            self.track_transition(agent.name, previous, new_state)

    def initiate_interaction(
        self,
        agent_name: str,
        input_data: str,
        emotion_delta: Optional[float] = None,
        debate_topic: Optional[str] = None,
    ) -> str:
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError("Agent not recognized")

        agent.perceive(input_data)
        if emotion_delta is not None:
            agent.update_emotion(emotion_delta)
            self.track_emotional_change(agent.name, agent.emotion)
        if debate_topic:
            self.track_philosophical_debate(agent.name, debate_topic)

        self.trigger_transition(agent)
        return agent.state
