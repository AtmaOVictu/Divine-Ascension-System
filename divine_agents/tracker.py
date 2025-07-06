"""Ontological tracker that houses all necessary agents."""

from typing import Dict, List

from .agent import Agent


class MasterEye(Agent):
    """Agent perceiving reality visually."""

    def perceive(self, input_data: str) -> str:
        return f"Mojster očesa zaznava: {input_data}"


class MasterEar(Agent):
    """Agent perceiving reality through sound."""

    def perceive(self, input_data: str) -> str:
        return f"Mojster ušesa zaznava: {input_data}"


class MasterSense(Agent):
    """Agent for subtle intuitive perception."""

    def perceive(self, input_data: str) -> str:
        return f"Mojster čuta zaznava: {input_data}"


class MasterBodySense(Agent):
    """Agent perceiving bodily sensations."""

    def perceive(self, input_data: str) -> str:
        return f"Mojster čutil telesa zaznava: {input_data}"


class OntologicalTracker:
    """Tracker acting as a nest for all required agents."""

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

    def trigger_transition(self, agent: Agent) -> str:
        previous = agent.state
        new_state = agent.transition()
        if previous != new_state:
            self.track_transition(agent.name, previous, new_state)
        return new_state

    def initiate_interaction(self, agent_name: str, input_data: str, emotion: float) -> str:
        agent = self.agents.get(agent_name)
        if not agent:
            return "Agent ni prepoznan!"
        perception = agent.perceive(input_data)
        self.track_philosophical_debate(agent_name, input_data)
        agent.update_emotion(emotion)
        new_state = self.trigger_transition(agent)
        self.track_emotional_change(agent_name, agent.emotion)
        return f"{perception} | novo stanje: {new_state}"
