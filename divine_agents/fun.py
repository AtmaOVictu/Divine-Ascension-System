"""Interactive modules for agent entertainment and decision making."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple

from .agent import Agent


@dataclass
class Question:
    question: str
    options: List[str]
    correct_index: int


class KvizZabavnost:
    """Simple quiz that can influence agent transitions."""

    def __init__(self) -> None:
        self._questions = [
            Question(
                question="Kaj pomeni prehod iz Ego v Jaz?",
                options=["Sprejemanje", "Prekinitev", "Sprememba"],
                correct_index=0,
            ),
            Question(
                question="Kaj je resnica v ontolo\u0161kem sistemu?",
                options=["Samospoznanje", "Fizikalna resni\u010dnost", "Absolutna gotovost"],
                correct_index=0,
            ),
            Question(
                question="Kaj pomeni prehod iz Enotnosti v Ego?",
                options=["Znova manifestiranje", "Zavra\u010danje realnosti", "Transformacija"],
                correct_index=0,
            ),
        ]
        self._current: Question | None = None

    def ask(self, index: int | None = None) -> Tuple[str, List[str]]:
        """Return a question and possible options. If index is provided the
        question is chosen deterministically."""
        if index is None:
            self._current = random.choice(self._questions)
        else:
            self._current = self._questions[index % len(self._questions)]
        return self._current.question, self._current.options

    def answer(self, choice_index: int) -> bool:
        """Check if selected answer is correct."""
        if not self._current:
            raise ValueError("No question asked")
        return choice_index == self._current.correct_index


class UgankaZabavnost:
    """Puzzle encouraging ontological reflection."""

    def __init__(self) -> None:
        self.riddle = "Kaj se zgodi, ko Ego preide v Jaz, vendar ne dose\u017ee Enotnosti?"
        self.solution = "Napetost v prehodu"

    def pose(self) -> str:
        return self.riddle

    def solve(self, answer: str) -> bool:
        return answer.strip().lower() == self.solution.lower()


class IgraOdlocanja:
    """Decision-based game influencing agent state."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def decision(self, proceed: bool) -> str:
        """Apply player's decision and transition agent if needed."""
        if proceed:
            self.agent.tension += 0.5
        else:
            self.agent.tension -= 0.3

        return self.agent.transition()

    def play(self, decisions: List[bool]) -> List[str]:
        """Play multiple rounds returning states after each decision."""
        states = []
        for d in decisions:
            states.append(self.decision(d))
        return states
