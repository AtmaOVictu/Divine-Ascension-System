"""Utility functions for ASCII-based word transformations."""

from typing import Dict


def ascii_table() -> Dict[str, int]:
    """Return a mapping of ASCII characters to their codes for values 0-127."""
    return {chr(i): i for i in range(128)}


def ionize_word(word: str) -> str:
    """Shift each character's ASCII code by 1 to transform the word."""
    transformed = "".join(chr(ord(ch) + 1) for ch in word)
    return transformed
