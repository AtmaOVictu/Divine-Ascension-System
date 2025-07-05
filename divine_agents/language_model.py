"""Language segmentation and integration utilities."""

from __future__ import annotations

from dataclasses import dataclass

from .agent import Agent


@dataclass
class LanguageModel:
    """Represents a modular language system for an agent.

    Parameters
    ----------
    language : str
        Active language of the model.
    agent : Agent
        Ontological agent associated with this language.
    """

    language: str = "sloven\u0161\u010dina"
    agent: Agent | None = None

    def __post_init__(self) -> None:
        if self.agent is None:
            self.agent = Agent(name=f"EJ-{self.language}")

    def transition_language(self, new_language: str) -> str:
        """Transition to a new language (\u039b)."""
        self.language = new_language
        self.agent = Agent(name=f"EJ-{new_language}")
        return self.confirm_transition(new_language)

    def confirm_transition(self, language: str) -> str:
        """Confirm language transition (\u221a)."""
        return f"\u221a: Prehod v {language} potrjen"

    def synthesis(self, *languages: str) -> str:
        """Integrate languages into a synthetic model (\u03a9)."""
        joined = ", ".join((self.language,) + languages)
        self.language = "sinteti\u010dni jezik"
        return f"\u03a9: Integracija {joined} -> {self.language}"
