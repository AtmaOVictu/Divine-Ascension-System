from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Transition:
    """Record of a state transition for an Agent."""

    timestamp: datetime
    previous_state: str
    new_state: str
    tension: float
    emotion: float


class History:
    """Container for transition history."""

    def __init__(self) -> None:
        self._transitions: List[Transition] = []

    def add(self, previous_state: str, new_state: str, tension: float, emotion: float) -> None:
        """Add a transition record."""
        self._transitions.append(
            Transition(
                timestamp=datetime.utcnow(),
                previous_state=previous_state,
                new_state=new_state,
                tension=tension,
                emotion=emotion,
            )
        )

    def get(self) -> List[Transition]:
        """Return list of transitions."""
        return list(self._transitions)
