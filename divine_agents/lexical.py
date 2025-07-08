import random
from typing import List


def generate_anagram(word: str) -> str:
    """Return a random anagram of the supplied word."""
    letters: List[str] = list(word)
    random.shuffle(letters)
    return "".join(letters)


def create_amalgamation(concept1: str, concept2: str) -> str:
    """Create a simple amalgamation from two concepts."""
    half1 = concept1[: len(concept1) // 2]
    half2 = concept2[len(concept2) // 2 :]
    return half1 + half2
