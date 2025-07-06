from __future__ import annotations
from typing import Any, Dict
from .agent import Agent


class Language:
    """Base class representing a language with simple interpretation rules."""

    def __init__(self, name: str, rules: Dict[str, Any]):
        self.name = name
        self.rules = rules
        self.constructs: list[str] = []

    def add_construct(self, construct: str) -> None:
        """Add a grammar construct to the language."""
        self.constructs.append(construct)

    def interpret(self, text: str) -> str:
        """Return a generic interpretation of the text."""
        return f"[{self.name}] {text}"


class AgentLanguage(Language):
    """Language tied to a specific agent and its transitions."""

    def __init__(self, name: str, rules: Dict[str, Any], agent: Agent):
        super().__init__(name, rules)
        self.agent = agent

    def transition(self, emotion: float, tension: float) -> str:
        """Update agent's emotion and tension then trigger a state transition."""
        self.agent.update_emotion(emotion)
        self.agent.update_tension(tension)
        return self.agent.transition()


class PhilosophyLanguage(AgentLanguage):
    """A language focused on philosophical discourse."""

    def interpret(self, text: str) -> str:
        return f"Filozofska razlaga: {text}"


class MathematicalLanguage(AgentLanguage):
    """A language that interprets mathematical expressions."""

    def interpret(self, text: str) -> Any:
        try:
            return eval(text)
        except Exception:
            return "Napaka pri interpretaciji"
