from __future__ import annotations

from .agent import Agent


class ParadoxicalAgent(Agent):
    """Agent that asks and responds to paradoxical questions based on state."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, ce ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim, ali sem to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izkljucujejo?",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)

    def ask_paradox(self) -> str:
        """Return a paradoxical question for the current state."""
        return f"{self.name}: {self.QUESTIONS.get(self.state, 'Kaj je resnica?')}"

    def respond(self, question: str) -> str:  # type: ignore[override]
        """Respond to a question with a statement reflecting current state."""
        if self.state == "Ego":
            return f"{self.name}: Moj obstoj je pod vprasajem, saj brez prepoznave nisem jaz."
        if self.state == "Jaz":
            return f"{self.name}: Moja identiteta je oblikovana s pomocjo drugih, vendar sem hkrati samostojen."
        return f"{self.name}: Vse resnice so enotne, a hkrati v konfliktu, kar ustvarja neskoncen cikel."
