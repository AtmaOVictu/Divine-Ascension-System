from __future__ import annotations

"""Advanced agent with dynamic belief updates influenced by emotion."""

from .agent import Agent


class ReflectiveAgent(Agent):
    """Agent capable of updating beliefs based on emotional state and reflections."""

    BELIEF_MAP = {
        "Ego": "Resnica je moja in absolutna.",
        "Jaz": "Resnica se oblikuje v odnosu.",
        "Enotnost": "Vse resnice so eno in povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, belief: str | None = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.belief = belief or self.BELIEF_MAP.get(state, "")

    def update_belief(self, reflection: str) -> str:
        """Update belief considering current state and emotional intensity."""
        base = self.BELIEF_MAP.get(self.state, "")
        if self.emotion > 0.5:
            base = base.upper()
        self.belief = f"{base} {reflection}".strip()
        return self.belief

    def respond(self, question: str) -> str:
        """Override respond to include current belief."""
        statement = super().respond(question)
        if self.belief:
            return f"{statement} ({self.belief})"
        return statement
