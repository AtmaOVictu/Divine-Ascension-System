"""Utility functions for translating text to binary and back."""

from typing import List


def text_to_binary(text: str) -> str:
    """Return the binary representation of ``text`` using 8-bit ASCII."""
    return " ".join(format(ord(ch), "08b") for ch in text)


def binary_to_text(binary: str) -> str:
    """Convert a binary string back to normal text."""
    return "".join(chr(int(b, 2)) for b in binary.split())
