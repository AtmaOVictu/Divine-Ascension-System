from __future__ import annotations
from datetime import datetime
from typing import List, Dict

from .agent import Agent


class ShortEgoRecorder:
    """Recorder tracking state transitions and their limitations."""

    def __init__(self) -> None:
        self.records: List[Dict[str, str]] = []
        self.limitations: List[str] = []

    def record_transition(self, agent: Agent, new_state: str) -> None:
        """Record a transition attempt and check for limitations."""
        transition_info = {
            "state_from": agent.state,
            "state_to": new_state,
            "emotion": str(agent.emotion),
            "tension": str(agent.tension),
            "transition_time": datetime.utcnow().isoformat(),
        }
        self.records.append(transition_info)
        self._check_limitations(agent, new_state)

    def _check_limitations(self, agent: Agent, new_state: str) -> None:
        """Identify if a limitation prevents the transition."""
        if new_state == "Jaz" and agent.tension < 0.5:
            self.limitations.append(
                f"Agent {agent.name} is limited by low tension to move to Jaz."
            )
        elif new_state == "Ego" and agent.emotion < 0.3:
            self.limitations.append(
                f"Agent {agent.name} cannot transcend to broader states due to low emotion."
            )

    def get_records(self) -> List[Dict[str, str]]:
        """Return all transition records."""
        return self.records

    def get_limitations(self) -> List[str]:
        """Return encountered limitations."""
        return self.limitations
