from .agent import Agent

class ParadoxicalAgent(Agent):
    """Agent that poses paradoxical questions based on its ontological state."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, če ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim o sebi, ali to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izključujejo?",
    }

    def ask_paradox(self) -> str:
        """Return a paradoxical question reflecting the current state."""
        question = self.QUESTIONS.get(self.state, "Kaj je resnica?")
        return f"{self.name}: {question}"

    def respond(self, question: str) -> str:  # type: ignore[override]
        """Return a state-based philosophical response."""
        base = super().respond(question)
        return f"{self.name}: {base}"
