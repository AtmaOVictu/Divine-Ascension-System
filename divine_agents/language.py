import random


def generate_anagram(word: str, seed: int | None = None) -> str:
    """Generate a deterministic anagram of a word."""
    rng = random.Random(seed)
    chars = list(word)
    rng.shuffle(chars)
    return ''.join(chars)


def create_amalgamation(concept1: str, concept2: str) -> str:
    """Create a simple amalgamation of two concepts."""
    return concept1 + concept2[len(concept2) // 3:]
