from typing import List, Dict

from .agent import Agent


class KvizZabavnost:
    """Simple quiz game affecting agent state."""

    def __init__(self) -> None:
        self.questions: List[Dict] = [
            {
                "question": "Kaj pomeni prehod iz Ego v Jaz?",
                "answers": ["Sprejemanje", "Prekinitev", "Sprememba"],
                "correct": 0,
            },
            {
                "question": "Kaj je resnica v ontološkem sistemu?",
                "answers": ["Samospoznanje", "Fizikalna resničnost", "Absolutna gotovost"],
                "correct": 0,
            },
            {
                "question": "Kaj pomeni prehod iz Enotnosti v Ego?",
                "answers": ["Znova manifestiranje", "Zavračanje realnosti", "Transformacija"],
                "correct": 0,
            },
        ]

    def ask(self, index: int, answer: int, agent: Agent) -> bool:
        """Check answer and update agent accordingly."""
        q = self.questions[index % len(self.questions)]
        correct = answer == q["correct"]
        if correct:
            agent.update_emotion(0.6)
        else:
            agent.update_emotion(0.2)
        agent.transition()
        return correct


class UgankaZabavnost:
    """Riddle that can trigger state changes."""

    def __init__(self) -> None:
        self.riddle = (
            "Kaj se zgodi, ko Ego preide v Jaz, vendar ne doseže Enotnosti?"
        )
        self.solution = "Napetost v prehodu"

    def solve(self, attempt: str, agent: Agent) -> bool:
        correct = attempt.strip().lower() == self.solution.lower()
        if correct:
            agent.update_emotion(0.6)
        else:
            agent.update_emotion(0.1)
        agent.transition()
        return correct


class IgraOdlocanja:
    """Decision game based on agent tension."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def make_decision(self, proceed: bool) -> str:
        if proceed:
            self.agent.update_tension(self.agent.tension + 0.8)
        else:
            self.agent.update_tension(max(0.0, self.agent.tension - 0.2))
        return self.agent.transition()
