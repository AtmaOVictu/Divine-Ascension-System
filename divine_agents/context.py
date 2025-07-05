from dataclasses import dataclass


@dataclass
class Context:
    """Represents internal and external influences on an agent."""

    inner: str = ""
    outer: str = ""
    philosophy: str = ""
