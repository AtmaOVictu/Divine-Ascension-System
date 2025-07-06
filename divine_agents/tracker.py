from typing import Dict, List

from .agent import Agent


class OntologicalTracker:
    """Track state transitions, emotions and debates between agents."""

    def __init__(self, agents: List[Agent]):
        self.agents: Dict[str, Agent] = {a.name: a for a in agents}
        self.transitions: List[Dict[str, str]] = []
        self.emotional_states: Dict[str, List[str]] = {}
        self.philosophical_debates: Dict[str, List[str]] = {}

    def track_transition(self, agent: Agent, old_state: str, new_state: str) -> None:
        self.transitions.append({"agent": agent.name, "from": old_state, "to": new_state})

    def track_emotion(self, agent: Agent) -> None:
        self.emotional_states.setdefault(agent.name, []).append(f"{agent.emotion_label}:{agent.emotion}")

    def track_debate(self, agent: Agent, topic: str) -> None:
        self.philosophical_debates.setdefault(agent.name, []).append(topic)

    def initiate_debate(self, agent1_name: str, agent2_name: str, topic: str) -> List[str]:
        """Simulate a debate and record all changes."""
        a1 = self.agents[agent1_name]
        a2 = self.agents[agent2_name]
        lines: List[str] = []

        # initial exchange
        lines.append(f"{a1.name} ({a1.state}): {a1.respond(topic)}")
        lines.append(f"{a2.name} ({a2.state}): {a2.respond(topic)}")
        self.track_debate(a1, topic)
        self.track_debate(a2, topic)

        # escalate emotions leading to potential transitions
        a1.update_emotion(0.8, "anger")
        a2.update_emotion(0.6, "curiosity")
        self.track_emotion(a1)
        self.track_emotion(a2)

        old1, old2 = a1.state, a2.state
        new1 = a1.transition()
        new2 = a2.transition()
        if new1 != old1:
            self.track_transition(a1, old1, new1)
        if new2 != old2:
            self.track_transition(a2, old2, new2)

        # final answers after transition
        lines.append(f"{a1.name} ({a1.state}): {a1.respond(topic)}")
        lines.append(f"{a2.name} ({a2.state}): {a2.respond(topic)}")
        return lines
