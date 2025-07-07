from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .agent import Agent


@dataclass
class OntoComputerUseAgent(Agent):
    """Agent capable of symbolic computer interactions."""

    server_url: str = ""
    actions: List[str] = field(default_factory=list)

    SYMBOLS: Dict[str, str] = field(
        default_factory=lambda: {"initiate": "∴", "transform": "∆", "resolve": "⊘"}
    )

    def execute_action(self, action: str, details: Optional[Dict[str, int | str]] = None) -> str:
        """Record a symbolic action representation."""
        details = details or {}
        start = self.SYMBOLS["initiate"]
        trans = self.SYMBOLS["transform"]
        end = self.SYMBOLS["resolve"]
        representation = f"{start}{action}{trans}{details}{end}"
        self.actions.append(representation)
        return representation
