"""Ontological agent model with emotional dynamics."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Tuple


class State(Enum):
    """Philosophical states of an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotions:
    """Container for basic emotions."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the maximum emotional intensity."""

        return max(self.fear, self.joy, self.anger)


@dataclass
class Agent:
    """Represents a debating agent."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotions: Emotions = field(default_factory=Emotions)

    def feel(self, **kwargs: float) -> None:
        """Update emotions and tension based on provided values."""

        for emotion, value in kwargs.items():
            if hasattr(self.emotions, emotion):
                setattr(self.emotions, emotion, value)
        self.tension = self.emotions.intensity()

    def update_state(self) -> None:
        """Trigger a state transition when thresholds are exceeded."""

        triggered = self.tension > 0.7 or self.emotions.intensity() > 0.5
        if self.state == State.EGO and triggered:
            self.state = State.JAZ
        elif self.state == State.JAZ and triggered:
            self.state = State.ENOTNOST

    def respond(self) -> str:
        """Return a statement reflecting the current ontological stance."""

        if self.state == State.EGO:
            return f"{self.name}: Truth is absolute and independent of others."
        if self.state == State.JAZ:
            return f"{self.name}: Truth is relative, shaped by our relationships."
        return f"{self.name}: All truths are one and interconnected."


@dataclass
class Debate:
    """Simple dialogue simulator for two agents."""

    agent1: Agent
    agent2: Agent

    def step(self) -> Tuple[str, str]:
        """Perform one dialogue step and update each agent."""

        self.agent1.update_state()
        self.agent2.update_state()
        return self.agent1.respond(), self.agent2.respond()

