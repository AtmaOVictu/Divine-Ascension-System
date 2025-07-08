from dataclasses import dataclass

@dataclass
class Frame:
    """Represents a snapshot of an agent's state within a frame/box."""
    state: str
    tension: float = 0.0
    emotion: float = 0.0
