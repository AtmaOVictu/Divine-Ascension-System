from .agent import Agent


class ParadoxicalAgent(Agent):
    """Agent that asks paradoxical questions based on its ontological state."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, ce ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim, ali sem to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izkljucujejo?",
    }

    def ask_paradox(self) -> str:
        """Return a paradoxical question for the current state."""
        question = self.QUESTIONS.get(self.state, "Kaj je resnica?")
        return f"{self.name}: {question}"

    def respond(self, question: str) -> str:
        """Respond philosophically along with the paradoxical question."""
        philosophical = super().respond(question)
        paradox = self.ask_paradox()
        return f"{philosophical} - {paradox}"
