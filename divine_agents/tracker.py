from typing import Dict, List, Optional

from .agent import Agent


class OntologicalTracker:
    """Track agents' states and emotional history."""

    def __init__(self, agents: List[Agent]):
        self.agents: Dict[str, Agent] = {agent.name: agent for agent in agents}
        self.transitions: List[Dict[str, str]] = []
        self.emotional_history: Dict[str, List[float]] = {
            agent.name: [agent.emotion] for agent in agents
        }

    def track_transition(self, agent: Agent, from_state: str, to_state: str) -> None:
        self.transitions.append({"agent": agent.name, "from": from_state, "to": to_state})

    def update_agent(
        self,
        name: str,
        emotion: Optional[float] = None,
        tension: Optional[float] = None,
    ) -> str:
        agent = self.agents[name]
        if emotion is not None:
            agent.update_emotion(emotion)
            self.emotional_history[name].append(agent.emotion)
        if tension is not None:
            agent.update_tension(tension)
        previous_state = agent.state
        new_state = agent.transition()
        if new_state != previous_state:
            self.track_transition(agent, previous_state, new_state)
        return new_state
