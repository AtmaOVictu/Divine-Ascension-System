import random
from typing import List

from .agent import Agent

class MultiColorAgent(Agent):
    """An Agent that also tracks color and visibility of its state."""

    COLOR_MAP = {
        "Ego": "Gray",
        "Jaz": "Blue",
        "Enotnost": "Gold",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.color = self.COLOR_MAP.get(state, "Gray")
        self.visibility = "Hidden"

    def toggle_visibility(self) -> None:
        """Toggle visibility between Visible and Hidden."""
        self.visibility = "Visible" if random.random() > 0.5 else "Hidden"

    def transition(self) -> str:
        """Transition state and update color/visibility when thresholds met."""
        previous = self.state
        new_state = super().transition()
        if new_state != previous:
            self.color = self.COLOR_MAP.get(new_state, self.color)
            self.toggle_visibility()
        return new_state

    def current_color(self) -> str:
        return self.color

    def current_visibility(self) -> str:
        return self.visibility

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = super().respond(question)
        if self.emotion > 0.7:
            prefix = "Strastno"
        elif self.emotion > 0.3:
            prefix = "Mirno"
        else:
            prefix = "Nevtralno"
        return f"{prefix}: {base}"


class MultiColorAgentSystem:
    """Manage a collection of MultiColorAgents."""

    def __init__(self, agents: List[MultiColorAgent]):
        self.agents = agents

    def transition_all(self) -> List[str]:
        lines = []
        for agent in self.agents:
            state_before = agent.state
            agent.transition()
            lines.append(
                f"{agent.name} from {state_before} -> {agent.state} ({agent.color}, {agent.visibility})"
            )
        return lines
