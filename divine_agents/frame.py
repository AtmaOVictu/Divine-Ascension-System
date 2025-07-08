from dataclasses import dataclass

@dataclass
class Frame:
    """Snapshot of an agent's state, emotion, and tension."""
    state: str
    emotion: float
    tension: float
