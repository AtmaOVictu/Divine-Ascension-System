from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue


def create_letter_agents(text: str) -> List[Agent]:
    """Create an Agent instance for each letter in the provided text."""
    return [Agent(letter) for letter in text]


def letter_dialogue(text: str) -> List[str]:
    """Generate dialogue lines for consecutive letter agents."""
    agents = create_letter_agents(text)
    lines: List[str] = []
    for idx in range(len(agents) - 1):
        lines.extend(philosophical_dialogue(agents[idx], agents[idx + 1]))
    return lines
