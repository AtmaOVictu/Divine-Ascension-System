"""Utility functions for text ionization."""


def ionize_word(word: str) -> str:
    """Shift each character by one in the ASCII table."""
    return "".join(chr(ord(c) + 1) for c in word)
