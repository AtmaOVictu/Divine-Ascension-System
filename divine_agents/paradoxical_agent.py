"""Agent capable of posing paradoxical questions and responding philosophically."""
from .agent import Agent


class ParadoxicalAgent(Agent):
    """Agent that explores paradoxes during state transitions."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, ce ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim o sebi, ali to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izkljucujejo?",
    }

    def ask_paradox(self) -> str:
        """Return a paradoxical question for the current state."""
        return f"{self.name}: {self.QUESTIONS.get(self.state, 'Kaj je resnica?')}"

    def respond(self, question: str) -> str:  # type: ignore[override]
        """Return a response influenced by the agent's state."""
        base = super().respond(question)
        return f"{self.name}: {base}"

