from __future__ import annotations

"""Utility for evaluating reasons behind agent transitions."""

from dataclasses import dataclass

from .agent import Agent


@dataclass
class LogarithmOfReason:
    """Calculate a textual reason based on an agent's state."""

    agent: Agent

    def calculate(self) -> str:
        """Return a message describing whether a transition is warranted."""
        reason_value = self.agent.tension * self.agent.emotion
        if reason_value > 0.5:
            return "Prehod je nujen, vendar premislimo o posledicah."
        if reason_value > 0.3:
            return "Prehod ni nujen, vendar raziskujmo možnost."
        return "Prehod je nepotreben, zadržimo se v trenutnem stanju."
