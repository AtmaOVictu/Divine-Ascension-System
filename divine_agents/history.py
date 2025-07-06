# -*- coding: utf-8 -*-
"""Agent variant that allows passing in a custom history."""
from __future__ import annotations

from typing import List

from .agent import Agent


class AgentWithHistory(Agent):
    """Agent that exposes history handling at initialization."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, history: List[str] | None = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.history = history if history is not None else [state]

    def transition(self) -> str:
        result = super().transition()
        self.history.append(result)
        return result
