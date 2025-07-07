from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

from .agent import Agent


@dataclass
class ShortEgoRecorder:
    """A recorder that tracks transitions and limitations."""

    records: List[Dict[str, object]] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)

    def record_transition(self, agent: Agent, new_state: str) -> None:
        """Record the agent's attempted transition."""
        info = {
            "state_from": agent.state,
            "state_to": new_state,
            "emotion": agent.emotion,
            "tension": agent.tension,
            "transition_time": datetime.now(),
        }
        self.records.append(info)
        self._check_limitations(agent, new_state)

    def _check_limitations(self, agent: Agent, new_state: str) -> None:
        if new_state == "Jaz" and agent.tension < 0.5:
            self.limitations.append(
                f"Agent {agent.name} is limited by low tension to move to Jaz."
            )
        elif new_state == "Ego" and agent.emotion < 0.3:
            self.limitations.append(
                f"Agent {agent.name} cannot transcend due to low emotion."
            )

    def get_records(self) -> List[Dict[str, object]]:
        return self.records

    def get_limitations(self) -> List[str]:
        return self.limitations
