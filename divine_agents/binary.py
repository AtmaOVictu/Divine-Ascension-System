"""Utility functions for binary representation."""

def text_to_binary(text: str) -> str:
    """Convert text to a space-separated binary string using 8-bit ASCII."""
    return " ".join(format(ord(ch), "08b") for ch in text)
