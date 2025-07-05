from dataclasses import dataclass, field
from typing import Dict


@dataclass
class World:
    """Represents the world or environment in which agents operate."""
    description: str = "Svet"


@dataclass
class Conscience:
    """Represents an agent's moral orientation."""
    moral_compass: float = 0.0


@dataclass
class Light:
    """Symbolic clarity or enlightenment."""
    intensity: float = 0.0


@dataclass
class Word:
    term: str
    meaning: str


class Language:
    """Simple dictionary-based language module."""

    def __init__(self) -> None:
        self._dictionary: Dict[str, str] = {}

    def add_word(self, word: str, meaning: str) -> None:
        self._dictionary[word.lower()] = meaning

    def meaning_of(self, word: str) -> str:
        return self._dictionary.get(word.lower(), "")

    def __contains__(self, word: str) -> bool:
        return word.lower() in self._dictionary
