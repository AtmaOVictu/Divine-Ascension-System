"""Multi-dimensional agent with moral dilemmas and state transitions."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class MultiDimensionalMoralAgent:
    """Agent that transitions between ontological states and makes moral decisions."""

    name: str
    ethics: str = "utilitarianism"
    emotion: float = 0.0
    tension: float = 0.0
    dimensions: int = 3
    state: str = "Ego"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition based on thresholds."""
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def moral_decision(self, others: List[MultiDimensionalMoralAgent] | None = None) -> str:
        """Return a moral decision string based on ethics and other agents."""
        if self.ethics == "utilitarianism":
            total_emotion = sum(a.emotion for a in others) if others else 0
            return "Maximize happiness" if total_emotion >= 0 else "Minimize suffering"
        if self.ethics == "deontology":
            return "Follow universal rules"
        if self.ethics == "virtue":
            return "Act virtuously"
        return "Seek justice"

    def philosophical_reply(self) -> str:
        """Return a statement about truth based on ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def dialogue_line(self, others: List[MultiDimensionalMoralAgent]) -> str:
        """Return a line of dialogue reflecting current state and moral decision."""
        decision = self.moral_decision(others)
        return f"{self.name} ({self.state}): {self.philosophical_reply()} Odločitev: {decision}"
