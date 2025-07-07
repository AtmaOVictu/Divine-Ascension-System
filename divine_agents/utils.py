"""Utility functions for safety checks and sanitization."""


def sanitize_output(output: str) -> str:
    """Sanitize potentially unsafe characters in text."""
    if not isinstance(output, str):
        raise ValueError("Output must be a string")
    return output.replace("<", "&lt;").replace(">", "&gt;")

