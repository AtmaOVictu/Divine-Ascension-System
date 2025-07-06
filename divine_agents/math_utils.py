import math

ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith('_')}
ALLOWED_NAMES.update({'pi': math.pi, 'e': math.e})


def evaluate_expression(expr: str) -> float:
    """Safely evaluate a mathematical expression using the math module."""
    return eval(expr, {"__builtins__": {}}, ALLOWED_NAMES)
