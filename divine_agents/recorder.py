"""ShortEgoRecorder module.

Tracks transitions between ontological states and notes limitations
when an agent lacks sufficient tension or emotion.
"""

from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class ShortEgoRecorder:
    """Recorder for transitions from Ego to Jaz and beyond."""

    def __init__(self) -> None:
        self.records: List[Dict[str, object]] = []
        self.limitations: List[str] = []

    def record_transition(self, agent: Agent) -> None:
        """Record an agent's transition and evaluate limitations."""
        state_from = agent.state
        state_to = agent.transition()
        info = {
            "state_from": state_from,
            "state_to": state_to,
            "emotion": agent.emotion,
            "tension": agent.tension,
        }
        self.records.append(info)
        self._check_limitations(agent, state_to)

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
