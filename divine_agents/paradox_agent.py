"""Agent with paradoxical questions and responses."""
from .agent import Agent

class ParadoxicalAgent(Agent):
    """Extension of :class:`Agent` that asks paradoxical questions."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, ce ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim o sebi, ali to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izkljucujejo?",
    }

    def ask_paradox(self) -> str:
        """Return the paradoxical question for the current state."""
        question = self.QUESTIONS.get(self.state, "Kaj je resnica?")
        return f"{self.name}: {question}"

    def respond(self, question: str) -> str:  # type: ignore[override]
        """Respond based on state and current emotional intensity."""
        base = super().respond(question)
        return f"{self.name} ({self.state}, custvo {self.emotion:.1f}): {base}"
