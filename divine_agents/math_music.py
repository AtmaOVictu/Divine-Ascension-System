"""Utility functions for mathematical and musical processing."""

from math import sin, cos, tan, pi, e, sqrt
from typing import List, Dict


_ALLOWED_NAMES: Dict[str, float] = {
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'pi': pi,
    'e': e,
    'sqrt': sqrt,
}


def evaluate_expression(expression: str) -> float:
    """Evaluate a simple mathematical expression using safe names."""
    return eval(expression, {"__builtins__": {}}, _ALLOWED_NAMES)


NOTES = ["C", "D", "E", "F", "G", "A", "B"]


def generate_scale(start: str, length: int) -> List[str]:
    """Generate a simple ascending scale of given length starting from a note."""
    if start not in NOTES:
        raise ValueError("Invalid start note")
    start_index = NOTES.index(start)
    return [NOTES[(start_index + i) % len(NOTES)] for i in range(length)]

