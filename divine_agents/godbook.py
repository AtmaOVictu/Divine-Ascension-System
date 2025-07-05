import time
from typing import List, Dict, Optional

class Godbook:
    """Stores a history of philosophical questions and answers."""

    def __init__(self) -> None:
        self.entries: List[Dict[str, str]] = []

    def add_entry(self, agent_name: str, state: str, question: str, answer: str) -> None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.entries.append({
            "timestamp": timestamp,
            "agent": agent_name,
            "state": state,
            "question": question,
            "answer": answer,
        })

    def display_entries(self) -> None:
        for entry in self.entries:
            print(f"{entry['timestamp']} - Agent {entry['agent']} ({entry['state']}):")
            print(f"Q: {entry['question']}")
            print(f"A: {entry['answer']}\n")


from .agent import Agent

class ParadoxicalAgent(Agent):
    """Agent that asks paradoxical questions and logs them to a Godbook."""

    QUESTIONS = {
        "Ego": "Ali sem jaz res, če ne prepoznam tistega, kar sem?",
        "Jaz": "Ali sem to, kar mislim, ali sem to, kar drugi mislijo o meni?",
        "Enotnost": "Kako lahko vse resnice obstajajo hkrati, ko se med seboj izključujejo?",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 godbook: Optional[Godbook] = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.godbook = godbook

    def ask_paradox(self) -> str:
        question = self.QUESTIONS.get(self.state, "Kaj je resnica?")
        answer = self.respond(question)
        if self.godbook:
            self.godbook.add_entry(self.name, self.state, question, answer)
        return f"{self.name}: {question}\n{answer}"

    def respond(self, question: str) -> str:  # type: ignore[override]
        if self.state == "Ego":
            return f"{self.name}: Moj obstoj je pod vprašajem, saj brez prepoznave nisem jaz."
        if self.state == "Jaz":
            return f"{self.name}: Moja identiteta je oblikovana s pomočjo drugih, vendar sem hkrati samostojen."
        return f"{self.name}: Vse resnice so enotne, vendar so hkrati v konfliktu, kar ustvarja neskončen cikel."

    def transition(self) -> str:  # type: ignore[override]
        state = super().transition()
        self.ask_paradox()
        return state
