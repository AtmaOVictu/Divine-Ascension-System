"""Entertainment modules for ontological agents.

This module defines simple games and puzzles that integrate
with the ontological agent system.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Dict

from .agent import Agent


@dataclass
class Question:
    text: str
    choices: List[str]
    correct: str


class KvizZabavnost:
    """Simple quiz that asks agents about ontological transitions."""

    def __init__(self) -> None:
        self.questions: List[Question] = [
            Question(
                text="Kaj pomeni prehod iz Ego v Jaz?",
                choices=["Sprejemanje", "Prekinitev", "Sprememba"],
                correct="Sprejemanje",
            ),
            Question(
                text="Kaj je resnica v ontolo\u0161kem sistemu?",
                choices=["Samospoznanje", "Fizikalna resni\u010dnost", "Absolutna gotovost"],
                correct="Samospoznanje",
            ),
            Question(
                text="Kaj pomeni prehod iz Enotnosti v Ego?",
                choices=["Znova manifestiranje", "Zavra\u010danje realnosti", "Transformacija"],
                correct="Znova manifestiranje",
            ),
        ]

    def select_question(self) -> Question:
        """Return a random question."""
        return random.choice(self.questions)

    def check_answer(self, question: Question, answer_index: int) -> bool:
        """Return True if the chosen answer is correct."""
        try:
            choice = question.choices[answer_index]
        except IndexError:
            return False
        return choice == question.correct


class UgankaZabavnost:
    """A simple puzzle encouraging ontological thinking."""

    riddle = "Kaj se zgodi, ko Ego preide v Jaz, vendar ne dose\u017ee Enotnosti?"
    solution = "Napetost v prehodu"

    @classmethod
    def check_solution(cls, answer: str) -> bool:
        return answer.strip().lower() == cls.solution.lower()


class IgraOdlocanja:
    """Decision game that modifies an agent's tension."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def decide(self, proceed: bool) -> float:
        """Apply a decision and update the agent's tension."""
        if proceed:
            self.agent.update_tension(self.agent.tension + 0.5)
        else:
            new_tension = max(0.0, self.agent.tension - 0.3)
            self.agent.update_tension(new_tension)
        self.agent.transition()
        return self.agent.tension
